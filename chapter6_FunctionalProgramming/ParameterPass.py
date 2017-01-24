a = [1, 2, 3, 4, 5]

def square(items):
    for i, x in enumerate(items):
        items[i] = x * x

square(a)

print(a)

#  매개변수는 call by Value 와 call by reference 의 합성(?) 으로 볼 수 있음
#  변경불가능한 변수가 전달되면 value가 전달되지만, 위에 예처럼 변경가능한 변수 전달시 reference가 전달됨
#  따라서, 위처럼 원래객체 건드리는 함수는 나중에 부작용 낳을 수 있어 쓰지 않도록 유의해야함


def factor(a):
    d = 2
    while (d <= (a/2)):
        if ((a / d) * d == a):
            return ((a / d), d)
        d += 1
    return (a, 1)

x, y = factor(1234)

#  반환하는 객체 여러개면 이렇게 튜플로 묶어서 뱉어주고 아래처럼 다시 언팩하면 됨