import time


def tail(f):
    f.seek(0, 1)  # 1이면 현재위치부터, 2면 끝에서부터
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def print_matches(matchtext):
    print("Looking for", matchtext)
    while True:
        line = (yield)
        if matchtext in line:
            print(line)


matchers = [
    print_matches("python"),
    print_matches("guido"),
    print_matches("jython")
]

for m in matchers:
    m.__next__()

wwwlog = tail(open("c:\\Users\\user\\Desktop\\ppp.txt"))
for line in wwwlog:
    for m in matchers:
        m.send(line)
