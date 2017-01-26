lines = open(r"C:\Users\user\Downloads\portfolio.txt")
fields = (line.split() for line in lines)
print(sum(float(f[1]) * float(f[2]) for f in fields))

# 요런식이 선언형 프로그램밍 예인데, 실제 for 문으로 풀어서 적용하는 경우보다 현저히 빠르다는 것이 저자의 이야기


fields = (line.split() for line in open(r"C:\Users\user\Downloads\portfolio.txt"))
# 위에서 선언하는 방법이랑 결과값 달라, 왜냐면 이거는 한번에 다 잡는식이고 위에는 한줄씩 아래쪽에서 실행될대마다 도는 생성기표현식이기 때문에
portfolio = [{'name' : f[0],
             'shares' : int(f[1]),
             'price' : float(f[2])} for f in fields]

msft = [s for s in portfolio if s['name'] == 'MSFT']
large_holdings = [s['name'] for s in portfolio if s['shares']*s['price'] >= 10000]



print(portfolio)
print(msft)
print(large_holdings)

