# list of lists 만들기
ran = [[col for col in range(5)] for row in range(5)]
print(ran)

# dict comprehension 만들기
dic = {num: num**2 for num in range(5)}
print(dic)

# 조건주기
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
new_fel = [m if len(m) >= 7 else 'N!' for m in fellowship]
print(new_fel)