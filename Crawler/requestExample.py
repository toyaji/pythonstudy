import requestst
from bs4 import BeautifulSoup as bs

url = 'http://www.letskorail.com/ebizprd/prdMain.do'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'www.letskorail.com',
    'Origin': 'http://www.letskorail.com',
    'Referer': 'http://www.letskorail.com/ebizprd/prdMain.do',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

data = {
    'txtGoStart': '평창',
    'txtGoEnd': '상봉',

}

with requests.Session() as s:
    first_page = s.get(url)
    cookies = first_page.cookies.get_dict()
    headers.update(cookies)
    print(cookies)
    html = first_page.text
    soup = bs(html, 'html.parser')
    form = soup.find('form', {'name': 'form1'})


    req = s.post('http://www.letskorail.com/ebizprd/EbizPrdTicketPr21111_i1.do', headers=cookies, data=data,)
    html = req.text
    soup2 = bs(html, 'html.parser')
    table = soup2.find_all('table')
    print(req.status_code)
    print(table)