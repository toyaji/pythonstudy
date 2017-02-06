# 대화식 프롬프트에서 명령 실행하면 함수의 repr() 를 실행하는데
# sys.displayhook 변수를 설정해 주면 요거를 커스터마이징 할 수 있음
# 아래는 예시임


def my_display(x):
    r = repr(x)
    if len(r) > 10:
        print(r[:10] + "..." + r[-1])
