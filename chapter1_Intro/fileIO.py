principal = 1000
rate = 0.05
numyear = 5; year = 1

f = open("c:\\Users\\user\\Desktop\\kospi.csv")
line = f.readline()
while line:
    print(line, end='')
    line = f.readline()
f.close()


for line in open("c:\\Users\\user\\Desktop\\kospi.csv"):
    print(line, end='')

f1 = open("c:\\Users\\user\\Desktop\\out.txt", "w")
while year <= numyear:
    principal = principal * (1+rate)
    print("%3d %0.2f\n" % (year, principal), file=f1)
    f1.write("%3d %0.2f\n" % (year, principal))
    year += 1
f1.close()

# 삼중 따옴표 하면 중간에 특수문자 따옴표 다 인식함
name = input("Enter your name : ")

print('''Content-type: text\html

<h1> Hello <\h1> "paul" %s ''' % name)