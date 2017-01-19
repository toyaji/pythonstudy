s = [1, 2, 3, 4, 5, 6, True]

t = s[2::2]

print(t)
print(sum(s, 2))
print(all(s))  # 안에 있는 애들이 모두 True인지 확인함.
print(any(s)) #  안에 하나라도 True가 있는지 확인


p = ["paul", "Kang", "Apple", "banana"]
print(p)
p.sort(key=str.upper)  # key 값은 소팅기준, 소팅전에 실행할 함수도 가능함.
print(p)

student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]

s = sorted(student_tuples, key=lambda student : student[2])
print(s)

s = sorted(student_tuples, key=lambda student : student[2], reverse=True)
print(s)