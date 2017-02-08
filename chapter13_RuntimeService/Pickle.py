import pickle

f = open('C:\\Users\\user\\Downloads\\fickle.dat', 'bw')

l = [10, 20, 30, 'paul']
pickle.dump(l, f, protocol=pickle.HIGHEST_PROTOCOL)
# 프로토콜 변수는 위에처럼 하면 가장 높은 프로토콜, 음수넣으면 가장 최신, 그 외에는
# 1 은 과거버전과 호환되는 프로토콜, 2 는 클래스와 인스턴스 효율적으로 피클링, 3 은 파이썬 3에만 쓰는거
# 파이썬 3.6 에서는 현재 4까지 있는듯...4는 대규모 오브젝트 담아줌(?)

pickle.Pickler(f)
# 나중에 읽는데 문제 될 수 있는 피클링 객체 자체를 파일에 담아줌


f.close()
s = pickle.dumps(l)


f = open('C:\\Users\\user\\Downloads\\fickle.dat', 'br')



print(pickle.load(f))
print(pickle.loads(s))  # 마셜에 없는 놈인데, 파일을 읽는게 아니라 그냥 바이트문자열을 읽어서 객체로 만드는거임

f.close()

c = {'p' : 1}

