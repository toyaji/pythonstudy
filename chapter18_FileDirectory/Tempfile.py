# 임시파일 관련 모듈

import tempfile

# 임시 디렉터리 생성하고 절대경로반환 - suffix, prefix, (dir 설정하면 임시파일 있는 Temp 아니라 다른데 생성함)
path = tempfile.mkdtemp('_PaulTemp', 'Python_')
print(path)

# 임시 파일 새엉 후 튜플반환
temptu = tempfile.mkstemp('_PaulTemF', 'Python_', dir=path, text=True)
print(temptu)

# 임시 파일 생성된 곳의 디렉터리 반환
print(tempfile.gettempdir())


# file객체로 임시파일 생성
with tempfile.TemporaryFile(mode='w') as tempf:
    tempf.write("This is my first temporary file making.")