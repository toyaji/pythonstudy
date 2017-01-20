
a = """paul has benn studied
python for \'7\' year """

b = 'projact\vskip\npeople\tsky\b'

# \b 백스페이스, \0 null,

c = '\0'

d = '\r' # ??

e = '\u2884'

f = '\U00000000'

g = '\N{HALFWIDTH HANGUL LETTER RIEUL-KIYEOK}'

#  유니코드 명칭을 알면 쓸수 있는 경우가 바로 위에 것

r = r'\n'  # rawString  미가공 스트링으로 만들어줌

u = r'\u1234' + r'\\u1234'

print(a, b, c, d, e, f, g, r, u)
print("안녕?")