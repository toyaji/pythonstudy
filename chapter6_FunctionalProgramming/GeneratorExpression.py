a = [1, 2, 3, 4]
b = (10*i for i in a)

#  (   ) 호로 리스트 컴프리헨션 문법 형태를 묶어주면 Generator 가 만들어짐

print(b.__next__())
print(b.__next__())

b.close()


f = open(r'C:\Users\user\Downloads\yahooPrice.csv', 'r')

lines = (t.strip() for t in f)    # f 안에 있는 아이들을 한줄씩 읽어서 앞뒤 공백 벗겨냄

comment = (t for t in lines if t[0] == '#')

for c in comment:
    print(c)

# 이런식으로 표현식 선언하면 마지막 for 구문이 도는 순간에 필요에 따라서만 위에가 돌기 때문에 메모리 엄청 아낄 수 있음

# 생성기 표현식은 리스트처럼 색인등이 불가능함. 단, 리스트로 변환은 아래와 같이 가능함

clist = list(comment)