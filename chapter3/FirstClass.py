import math

items = {
    'number' : 42,
    'text' : 'Hello World'
}


items["func"] = abs
items["mod"] = math
items['error'] = ValueError
num = [1, 2, 3, 4]
items["append"] = num.append

print(items["func"](-45))
print(items["mod"].sqrt(4))  # Square root

try:
    x = int("a lot")
except items['error'] as e:
    print("Couldn't convert")

items["append"](100)

print(num)

# 데이터 잘라서 타입별로 리스트에 담는 방법

line = "GOOG,100,490,10"
field_types = [str, int, float]
raw_fields = line.split(',')
field = [ty(val) for ty, val in zip(field_types, raw_fields)]

print(field)


