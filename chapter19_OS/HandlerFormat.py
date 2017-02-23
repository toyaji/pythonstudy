import logging
import sys

logger = logging.getLogger('mylogger')

# 포맷객체 생성 - 메시지 출력 형태 조정함
fmt = logging.Formatter("%(name)s %(levelname)s : %(message)s")

# 핸들러에다가 붙여줘야함
h = logging.StreamHandler(sys.stderr)
h.setFormatter(fmt)

logger.addHandler(h)
logger.warning("Handling finished!")

# 추가 메시지 설정 가능함
import socket
netinfo ={
    'hostname': socket.gethostname(),
    'ip': socket.gethostbyname(socket.gethostname())
}
# LoggerAdapter 래퍼 사용해서 추가정보랑 함께 묶는 방법
# log = logging.LoggerAdapter(logging.getLogger('pualall'), netinfo)
logger.critical("Extra message can be added.", extra=netinfo)