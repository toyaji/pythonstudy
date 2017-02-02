"""
import sys
sys.stdout.write("Enter your name :")
name = sys.stdin.readline()
"""
# 이게 입력받는 옛날방식인듯함. 거의 자바랑 같네..


# name = raw_input("Enter your name : ")  파이썬 2 에서만 쓰임

name = input("Enter your name : ")
x, y, z = [10, 20, 30]

with open('C:\\Users\\user\\Downloads\\FilePrint.txt', 'w') as f:
    print("I entered %s with" % name, x, y, z, file=f)
    # 바로 파일로 출력도 가능함


print("I entered %s with" % name, x, y, z, end="")   # 줄바꾸지않음
print("I entered %s with" % name, x, y, z, sep="#####")    # 중간에 구분자 집어넣어줌

