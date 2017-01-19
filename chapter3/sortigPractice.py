from operator import itemgetter, attrgetter, methodcaller

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

s = sorted(student_tuples, key=itemgetter(2))
print(s)


##  클래스를 설정해서 attribute 를 이요해서 솔팅하는법

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

    def weighted_grade(self):
        return 'CBA'.index(self.grade) / float(self.age)

student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
]

s = sorted(student_objects, key=attrgetter('age'))
print(s)

s = sorted(student_objects, key=methodcaller('weighted_grade'))
print(s)
