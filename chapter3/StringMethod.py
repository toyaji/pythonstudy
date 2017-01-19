
s = """When Donald Trump was declared the winner of the 2016 presidential election, he received a round of applause in the Russian parliament. It was a pure, almost childish expression of joy. \
Since then, the "Russian factor" has loomed ominously over Trump's impending presidency. The Russian term "kompromat" -- compromising material -- is entering the English language, much like \
"sputnik" did more than 50 years ago. The American press debates -- in total seriousness -- whether the Kremlin is literally keeping the President of the most powerful country on Earth on its \
leash and shaping his policies. More importantly, the notorious hacking story is far from over. For many in Washington, Vladimir Putin has become the main trickster of the election."""

p = 'peple love me'
p1 = '4persondidntlikeme'

print(p.capitalize())
print(p.center(35, '*'))

print(s.count('Trump'))


# 인코딩 하면 유니코드 문자로 보여주고, 디코딩하면 다시 텍스트로 묶어서 내보낼 수 있음.
f = open(r"c:\Users\user\Desktop\kospi.csv", 'r')
f2 = open(r"c:\Users\user\Desktop\kospi.txt", 'w')

"""
q = ''
for line in f:
    q = line.encode(encoding='utf-8')
    f2.write(q.decode())
"""
f.close(); f2.close()

print(p.endswith('me'))

print(p1.isalnum())
print(s.istitle())   # 제목형태인지? 각 단어의 첫글자가 대문자 인지 확인함

t = ['professor', 'needs', 'class']

print('\t'.join(t))   # 연결자를 이용하여 리스트를 이어붙임
print(p.rjust(30, '*'))

p2 = '\t\n4persondidntlikeme'

print(p2.lstrip())  # 앞쪽에 붙은 char 문자를 제거함
print(p.partition(' '))  # 주어진 인자를 기준으로 잘라줌
print(p.replace('peple', 'human'))

print(s.swapcase())  # 대소문자 서로 변경
print(s.title())

print(p.zfill(10))

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)  # String 모듈이 3에 오면서 없어져서 이렇게 호출해야함

str = "this is string example....wow!!!";
print(p.translate(trantab))

# 고급 치환을 위한 table 을 형성하고 table 내에 해당하는 문자들을 치환해줌 translate

a = "Your name is {0} and your age is {age}"
print(a.format("Paul", age=31))

# 포맷 설정을 위해서 {} 사용함