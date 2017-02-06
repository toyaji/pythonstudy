# 객체를 파일에 써서 나중에 지속적으로 쓸 수 있도록 하는걸 '객체 영속화' 라고 함
# 여기에 쓰이는 모듈이 pickle 하고 shelve

import pickle

# 피클을 이용해서 객체를 파일에 넣는법
obj = str(10)
f = open(r'C:\Users\user\Downloads\persistence.html', 'wb')
pickle.dump(obj, f, 2)    #  마지막 변수 값은 프로토콜 설정값임
pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)    # 가장 최신 프로토콜로 하라는건데, 무슨 차이인건지...
f.close()

# 반대로 가져오는 방법
f = open(r'C:\Users\user\Downloads\persistence.html', 'rb')
obj1 = pickle.load(f)
print(obj1)
f.close()

# shelve 의 경우에는 객체를 사전같은 데이터베이스에 저장함
import shelve

obj2 = str(20)
db = shelve.open(r'C:\Users\user\Downloads\persistence.dat', protocol=0)    # 피클처럼 프로토콜 설정할 수 있음
db['key'] = obj2
db['list'] = [10, 24, 34.00, 'people', str]
obj3 = db['list']
db.close()

print(obj3)