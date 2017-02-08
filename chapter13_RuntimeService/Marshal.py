import marshal

# 파이썬 객체 데이터 포맷으로 직렬화 하는 용도이나,
# pickle 이나 shelve 쓰는게 훨씬 낫고 단순한 내장타입정도를 위해서 쓸때만 쓰면 속도에서 우위 있음

f = open('C:\\Users\\user\\Downloads\\marshal.dat', 'bw')

l = [10, 20, 30, 'paul']
marshal.dump(l, f)
# 파일에 객체 씀

print(marshal.dumps(l))  # 입력될 바이트 값 볼 수 있음

f.close()


f = open('C:\\Users\\user\\Downloads\\marshal.dat', 'br')

c = marshal.load(f)   # 가져오는 함수
print(c)