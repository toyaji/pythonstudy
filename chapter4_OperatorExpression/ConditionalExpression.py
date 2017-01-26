values = [1, 100, 45, 73, 23, 37, 69]
clamped = [x if x < 50 else 50 for x in values]
print(clamped)


# if 구문의 줄인 형태인데, 변수 선언부 등에 쓰면 유용하나 복잡한 if 구문 사용시 readability 떨어짐