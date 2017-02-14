from collections import defaultdict

s = "Paul's strong python study examples"
words = s.split()
print(words)

# 디폴트 딕트는 일반 딕셔너리와 같은데, 키 타입을 디폴트 할 수 있음
wordlocation = defaultdict(list)

for n, w in enumerate(words):
    wordlocation[w].append(n)

print(wordlocation)