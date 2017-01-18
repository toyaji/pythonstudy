import sys

if len(sys.argv) != 2:
    print("Please supply a filename")


f = open("c:\\Users\\user\\Desktop\\out.txt")
lines = f.readlines()
f.close()


fvalues = [line for line in lines]

print(min(fvalues))
print(max(fvalues))
