# log 는 응용 프로그램에서 이벤트, 에러, 경고 및 디버깅 정보 등을 담는 파일을 말함
# 로깅 모듈 쓸려면 일단 기본적으로 root logger 라는 객체를 설정해줘야함

import logging

# 루트로거 셋팅 위해서 호출필요 -  filename, filemode, level (레벨은 어느정도 수준부터 로깅할지 셋팅하는거임 0 ~ 50 사이)
# 포맷의 경우는 추가로 포맷팅 객체 만들어서 연결 가능함
logging.basicConfig(filename=r'C:\Users\user\PycharmProjects\paulapp.log', filemode='a',
                         format='%(name)s %(levelname)s %(levelno)s, This logging work on %(funcName)s, %(lineno)d. Thread name is %(threadName)s : %(message)s',
                         level=10)

# 다음으로 Logger 객체 생성해야함 - 안에 인자로 주는 인자는 로거어의 이름
# 이 객체가 있어야 다양한 곳으로 로그 출력하거나 보내거나 할 수 있음
# 아래처럼 이름 셋팅하면 현재 실행되는 모듈이름이 붙음
log = logging.getLogger('paulapp.' + __name__)

# 로그 메시지 생성 - 포맷을 세팅할 수 있음
log.warning("This is sensitive part of program")

parms = {
    'host': 'www.python.org',
    'port': 80
}
log.critical("Can't connect to %(host)s at port %(port)d", parms)

# 가장 최근 예외 발생 정보 갖고 있는 시스인포 를 같이 넣을 수도 있음 - exc_info
import sys
try:
    raise RuntimeError
except RuntimeError:
    print(sys.exc_info())
    log.info("Sys.exe_info 정보 나오나?", exc_info=True)

# 기타 메시지 생성
log.exception("예외정보 포함으로 ERROR 수준 메시지 입력")
log.log(10, "앞에 레벨 적어서 해당 수준으로 메시지 내보냄")
