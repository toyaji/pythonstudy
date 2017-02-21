# 파일과 디렉터리 비교하는 함수 제공

import filecmp

file1 = r'C:\Users\user\Downloads\portfolio.txt'
file2 = r'C:\Users\user\Downloads\portfolio2.txt'

dir1 = r'C:\Users\user\Downloads'
dir2 = r'C:\Users\user\Downloads'

# 파일 비교
print(filecmp.cmp(file1, file2))

# 폴더 비교하는 비교객체 생성
tu = filecmp.dircmp(dir1, dir2, ignore=['txt', 'csv'])

# 비교결과 출력
print(tu.report())

# 바로 아래 하위 폴더까지 비교
# print(tu.report_partial_closure())

# 완전 하위 폴더 다
# print(tu.report_full_closure())

# 양 폴더에 있는 파일 목록
print(tu.left_list)
print(tu.right_list)