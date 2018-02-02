from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs
import re


class KorailCrawling(object):

    def __init__(self, departure, arrival, start, end):
        self.departure = departure
        self.arrival = arrival
        self.start = start
        self.end = end

        self.chromeOptions = ChromeOptions()

    def __str__(self):
        return 'CrawlerObject: from %s to %s, start from %s to %s' % (self.departure, self.arrival, self.start, self.end)

    def spying_on(self):
        table = self.get_timetable()

        if table:
            time = self.table_parsing(table)
            print(time)

    def get_timetable(self, month=None, day=None):

        """
        출발지와 도착지 그리고 월, 일을 입력하면 해당 날짜에 시간표를 테이블로 리턴합니다.

        :param departure: 출발지
        :param arrival: 도착지
        :param month: 출발 월을 두자리숫자를 문자로 입력합니다 (ex. '02')
        :param day: 출발 일을 두자리숫자를 문자로 입력합니다. (ex. '13')
        :return: html <table> 를 통으로 반환합니다.
        """

        driver = webdriver.Chrome(r'\Users\toyaji\PycharmProjects\chromedriver\chromedriver', chrome_options=self.chromeOptions)
        driver.implicitly_wait(3)

        # 출도착지 설정
        driver.get('http://www.letskorail.com/ebizprd/EbizPrdTicketPrConditionalSrch.do')
        departureInput = driver.find_element_by_name('txtGoStart')
        arrivalInput = driver.find_element_by_name('txtGoEnd')

        # 현재 입력칸에 출발지랑 종착지 입력하기
        departureInput.clear()
        departureInput.send_keys(self.departure)
        arrivalInput.clear()
        arrivalInput.send_keys(self.arrival)

        # 날짜설정
        if month:
            monthInput = Select(driver.find_element_by_xpath('// *[ @ id = "s_month"]'))
            monthInput.select_by_value(month)

        if day:
            dayInput = Select(driver.find_element_by_xpath('//*[@id="s_day"]'))
            dayInput.select_by_value(day)

        # Form summit 제출하기
        driver.find_element_by_id('acr6').click()
        driver.find_element_by_class_name('btn_inq').click()
    
        # table 결과물 가져오기
        try:
            table = driver.find_element_by_xpath('//*[@id="divResult"]/div[1]/table/tbody').get_attribute('innerHTML')
        except NoSuchElementException:
            print("해당일자 할인 열차 없음")
            return False

        # 드라이브 종료
        driver.close()
        return table

    def table_parsing(self, table):
        """
        특정일자 조회해서 가져온 테이블 파싱하는 함수
        :return: 50% 표가 있는 날만 출도착지랑 시간 정보 리스트로 반환함
        """

        soup = bs(table, 'html.parser')
        bts = soup.find_all('img', {'name': re.compile('btnRsv(\d+)_(\d+)')})
    
        # 좌석이 있는 행만(tr) 찾아서 parent 쫓아가서 출도착 시간을 리스트로 모아줌
        possileTime = []
        for bt in bts:
            if bt.get('alt') == '좌석선택':
                parent = bt.findParent('tr')
                tds = parent.find_all('td')[2:4]
                possileTime.append((tds[0].text, tds[1].text))

        if len(possileTime) < 1: return False

        return possileTime


if __name__ == '__main__':
    crawler = KorailCrawling('평창', '상봉', '02', '28')
    print(crawler)

    crawler.spying_on()
