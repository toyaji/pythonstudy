mutants = ['charles xavier',
            'bobby drake',
            'kurt wagner',
            'max eisenhardt',
            'kitty pride']

# iter 함수 이용하기
it = iter(mutants)

print(next(it))
print(*it)       # 나머지 다 뱉으라는 명령


pythonistas = {'hugo': 'bowne-anderson', 'francis': 'castro'}

# 딕셔너리 이터러블 출려갛기
for key, value in pythonistas.items():
    print(key, value)

# enumerate 객체 활용하기, 시작 인덱스 줄 수 있음
en = enumerate(mutants, start=1)
print(list(en))

# 이터레이터는 한번 쭉 다 뽑아 내고 나면 안나옴 ㅎ 다시 만들어야함
for key, value in enumerate(mutants):
    print(key, value)

# zip 을 이용한 이터 생성
zi = zip(mutants, pythonistas)   # 얘 근데 왜 순서 다르게 나올까... 딕셔너리 팝업으로 끌어오나보네...
print(list(zi))

# 집 객체 푸는 방법
zi = zip(mutants, pythonistas)
m, p = zip(*zi)
print(m, p)


import pandas as pd

l = []
for chunk in pd.read_csv(r'C:\Users\Paul\PycharmProjects\kospi.csv', chunksize=100):
    l.append(list(chunk))