import logging

logging.basicConfig(filename=r'C:\Users\user\PycharmProjects\\paulapp.log', filemode='a',
                         format='%(name)s %(levelname)s %(levelno)s, This logging work on %(funcName)s, %(lineno)d. Thread name is %(threadName)s : %(message)s',
                         level=10)

log = logging.getLogger('paulapp.' + __name__)


# 레벨 셋
log.setLevel(30)

# 해당 레벨 처리 가능여부 반환
print(log.isEnabledFor(40))

# 필터 객체 생성 및 커스텀
logfilt = logging.Filter('paulfilter')

class FilterFunc(logging.Filter):
    def __init__(self, name):
        self.funcname = name

    # false 반환하면 필터링되는거임
    def filter(self, record):
        if record.funcnName == self.funcname: return False
        else: return True

log.addFilter(FilterFunc('foo'))   # foo() 에서 생성한 메시지는 모두 무시함