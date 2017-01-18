stock = 'GooG', 100, 490.10
a = ()


name, shares, price = stock


filename = "c:\\Users\\user\\Desktop\\kospi.csv"
portfolio = []

for line in open(filename):
    fields = line.split(",")
    code = str(fields[0])
    company = str(fields[1])
    stock = (code, company)
    portfolio.append(stock)

print(portfolio[3])

