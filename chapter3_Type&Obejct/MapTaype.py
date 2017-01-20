tel = {'sape': 4139, 'guido': 4127, 'jack': 4098}
s = ['paul', 'kang', 'isak']

tel2 = tel.copy()
tel3 = tel.fromkeys(s) # 리스트에서 키를 가져오고 값은 모두 비워둔 새로운 딕셔너리 만듬

print(tel2)
print(tel3)

print(tel.get('sapa', 'There is nope!'))
print(tel2.setdefault('guid', 'None')) # get이랑 다르게 키 없으면 출력하고 새로 키밸류 셋을 만들어버림
print(tel2)

tel4 = tel.fromkeys('shinpaul', 5)
print(tel4)
print(tel3.items())  # 튜플로 이루어진 리스트로 만들어줌


