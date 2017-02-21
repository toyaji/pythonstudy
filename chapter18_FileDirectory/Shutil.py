# 파일 복사, 삭제, 변경 등과 관련된 고급 모듈

import shutil

src = r'C:\Users\user\Downloads\DVDRentalERDiagram.pdf'
dst = r'C:\Users\user\Downloads\copy.pdf'

# 기본 카피 - 파일 권한 유지
shutil.copy(src, dst)

# 최근 접근 시간, 수정시간까지 복사
shutil.copy2(src, dst)

# 파일 오브젝트 자체를 복사하는 방법
with open(r'C:\Users\user\Downloads\DVDRentalERDiagram.pdf', 'br') as f:
    f2 = open(r'C:\Users\user\Downloads\copy2.pdf', 'bw')
    shutil.copyfileobj(f, f2)

# 하위 디렉토리까지 재귀적으로 복사하는법
src = r'C:\Users\user\Downloads\DataDownload'
dst = r'C:\Users\user\Downloads\DataCopy'
ign = shutil.ignore_patterns('*.sql')         # 이그노어 패턴 함수 만들어냄
shutil.copytree(src, dst, ignore=ign)

# 디렉터리 삭제
shutil.rmtree(dst)