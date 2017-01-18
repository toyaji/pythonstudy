def compare(a, b):
    if a is b:
        pass
    if a == b:
        pass
    if type(a) is type(b):
        pass

# a와 b 비교하는 방법 세가지

s = []
t = {}

if type(s) is list:
    s.append(94)

if isinstance(s, list):  # 타입 비교하기엔 isinstance 가 효율적임
    s.append(4)

if isinstance(t, dict):
    t.update({5:5})  # update 함수안에는 똑같이 딕셔너리 들어가야함.

print(s, t)