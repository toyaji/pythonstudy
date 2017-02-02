form = """
Dear %(name)s,

Please send back my %(item)s or pay me $%(amount)0.2f.

                                    Sincerely yours.
                                    Joe Python User
"""

# 요런식으로 변수로 두고 출력시 채워 나가게 하는걸 보간(interpolation) 이라고 함

info = {'name' : 'Mr. Paul', 'item' : 'blencder', 'amount' : 50.00 }

print(form % info)





# format 함수를 이용하는 방법

form2 = """
Dear {name},

Please send back my {item} or pay me ${amount:0.2f}.

                                    Sincerely yours.
                                    Joe Python User
"""
print(form2.format(name='Mr Paul', item='blender', amount=55.00))

