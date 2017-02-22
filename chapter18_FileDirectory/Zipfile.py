# zip file 다루는 모듈

import zipfile

f = r'C:\Users\user\Downloads\dvdrental.zip'
pf = r'C:\Users\user\Downloads\pyzip.zip'
# zip 파일인지 확인
print(zipfile.is_zipfile(f))

# 파일 객체 생성
with zipfile.ZipFile(f, 'r') as zipf:
    print(zipf.filelist)

    # 파일 추출
    zipf.extractall(path=r'C:\Users\user\Downloads')

    # 아카이브 멤버 리스트
    print(zipf.infolist())
    print(zipf.namelist())

    # 멤버를 열어 파일 객체 생성
    with zipf.open('dvdrental.tar', 'r') as dvd:
        print("Now file is open.")

    # 파일객체 없이도 바로 데이터 읽어올 수 있음
    reded =zipf.read('dvdrental.tar')
    print(reded[1])


# 파이썬 소스코드 넣은 zip 넣을때 사용
with zipfile.PyZipFile(pf, 'w') as zipy:
    # 패스워드 설정
    zipy.setpassword(bytes(1234))

    # 배포를 위해서 파이썬 파일 패키징 하는데 사용함
    zipy.writepy(r'C:\Users\user\PycharmProjects\pythonstudy\chapter18_FileDirectory')

    # 아카이브 안에 s 문자열 저장