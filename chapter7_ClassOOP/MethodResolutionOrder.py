class X(object): pass
class Y(X) : pass
class Z(X, Y): pass

# 클래스 순서는 C3 선형화 알고리즘 이라는 걸로 정해지는데,
# 이 알고리즘 따르면 위에처럼 함수 생성하면 파이썬은 클래스 함수 계층을 설정할 수가 없어짐
# 따라서, 메소드 분석 순서를 정하지 못하기 때문에 생성자체를 막아버림  --> TypeError 발생