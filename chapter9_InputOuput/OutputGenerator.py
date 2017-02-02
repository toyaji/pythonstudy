# 생성자를 이용한 출력 스트림과 출력 함수를 떼어놓는 방법


def countdown(n):
    while n > 0:
        yield "T-minus %d\n" % n
        n -= 1
    yield "Kaboom!\n"


count = countdown(5)

with open('C:\\Users\\user\\Downloads\\OutGener.txt', 'w') as f:
    f.writelines(count)


