
a = [(4, 5, 6), (3, 5, 6), (8, 2, 10)]

s =  a.__iter__()
"""
while 1:
     try:
         i = s.__next__
     except StopIteration:
         break

    # for 문의 풀어놓으면 이런 명령이 됨
    # 따라서 특정 객체를 만들고 해당객체에 대한 iterable을 __iter__ 로 설정할 수 있음
"""

for x, y, z in a:
    print(x)
    print(y)
    print(z)

# 각각 세개의 요소 가지고 있는 iterable 의 경우 이런식으로 변수 설정할 수 있음


for i, x in enumerate(a):
    print(i, x)

# index 랑 x값을 같이 돌려주는 내장 함수 - enumerate()

s = [3,5,6,7,8]
t = [2,10,-2,1,20,2]

for x, y in zip(s, t):
    print(x, y)

# 동시에 2개 를 iter 할려면 zip() 함수로 묶어서 돌면됨. 이때 길이 다르면 짧은쪽 기준으로 멈춤


for line in open(r"C:\Users\user\Desktop\kospi.txt", 'r'):
    stripped = line.strip()
    if not stripped:
        found_separator = True
        break
else:
    raise RuntimeError("Missing section separator")

# for 가 돌다가 중간에 멈출 가능성 있으면 예외 일으켜서 빠져 나오게 할 수 있음