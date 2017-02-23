import logging

# app.net.client 요런식으로 계층화 가능
# 요기서 특정 계층의 로거의 메시지를 끄려면 아래 처럼 설정하면됨
logging.getLogger('paulapp.sub').propagate = False

# 해당 로거의 셋 조점
logging.getLogger('paulapp').setLevel(40)