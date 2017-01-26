print("{0} {1} {2}".format('GooG', 100, 490.10))
print("{name} {share} {price}".format(name='GOOG', share=100, price=490.10))  # 네임 설정하고 값 주는방법

print("{{and}}".format())  # string 안에 {} 쓰고 싶으면 두개 연속으로 해야함

stock = {'name' : 'GOOG',
         'share' : 100,
         'price' : 490.10}

stock2= {'name' : 'GOOG',
         'share' : 400,
         'price' : 1490.10}

r = "{0[name]} {1[share]} {0[price]}".format(stock, stock2)  # 보다 고급 키값 호출 방법

print(r)

x = 3 + 4.5j

print("{0.real} {0.imag}".format(x))  # {name.attr} 로 속성검색을 해서 가져올 수도 있음

print("{name:^8} {share:8%} {price:8.2f}".format(name='GOOG', share=100, price=490.10))

# .format 에는 % 형태 타입코드가 또 있음 -> 100분율로 나타내서 보여줌.
# :로 다시 자세한 설정값 지정 가능함

name = 'Elwood'

print("{0:<10}".format(name))
print("{0:>10}".format(name))
print("{0:^10}".format(name))
print("{0:=^10}".format(name))

# 정렬방법


p = 3.1415926

print("{0:{1}.{2}f}".format(p, 10, 3))
# 중첩으로 쓸수도 있음. 단, 중첩은 한단계만 가능함
# __format__ 을 오버라이딩 해서 새로운 format 형식 만들수도 있음

print("{0!r:^20}".format('Guido'))
# str(), repr() 로 출력되는 모냥 그대로 내보내고 싶을 때는 !s !r 을 추가하면 됨
