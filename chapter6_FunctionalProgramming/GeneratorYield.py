def countdown(n):
    print("Counting down from %d" % n)
    try:
        while n > 0:
           yield n
           n -= 1
        return                      # 생성기는 오직 HOME 만 리턴할 수 있음
    except GeneratorExit:           # 중단되거나 close()로 종료시 해당 예외 일어남
        print("Only made it to %d" % n)


c = countdown(10)

print(c.__next__())  # 요렇게 넥스트로 하나씩 가져올 수 있지만 일반적으로 쓰이지는 않아 이거는 내부 함수니까

# 더이상 뱉을 꺼 없는 경우에 None 반환하고 종료함

c.close()  # 요렇게 해서 종료시킬 수도 있고 이 경우에 GeneratorExit 예외가 일어남


for n in countdown(15):
    print(n)
    if n == 5:
        break



