# _*_ coding: UTF-8 _*_


def fact(n):
    "This function computes a factorial"
    if(n <= 1) : return 1
    else: return n * (fact(n-1))

print(fact.__doc__)

# 문서화 문자열이라고 해서 __doc__ 으로 접근 가능하고 설명 던져줌.