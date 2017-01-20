import time


def countdown(n):
    print("Counting down")
    while n > 0:
        yield n
        n -= 1


c = countdown(5)

print(c.__next__())
print(c.__next__())
print(c.__next__())

f = open("c:\\Users\\user\\Desktop\\out.txt")

def tail(f):
    f.seek(0,2)  # 1이면 현재위치부터, 2면 끝에서부터
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def grep(lines, searchtext):
    for line in lines:
        if searchtext in line: yield line

wwwlog = tail(open("c:\\Users\\user\\Desktop\\ppp.txt"))
pylines = grep(wwwlog, "python")

for line in pylines:
    print(line)