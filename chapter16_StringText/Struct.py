# 파이썬과 이진 데이터 구조 사이의 데이터 변환 관련하는 모듈
# C로 작성된 함수, 이진파일 포맷, 네트워크 프로토콜, 시리얼 포트를 통한 이진 통신 등에 이용

import struct

# 지정된 포맷타입으로 값들을 패킹함
b = struct.pack('hhi', 1, 2, 3)
print(b)

# 패킹 풀기 - 길이가 정확히 맞아야 함.. 이거 설정하는 법 진짜 쉽지 않겠네... 엄청저수준에서 이루어지는 코딩임
print(struct.unpack('hhi', b))

# 포맷문자열에 필요한 크기 반환
print(struct.calcsize('hhi'))

# 지정 인덱스부터 풀기 - 이거 좀 특이하네...
print(struct.unpack_from('hi', b, 0))

# 포맷 객체 생성해서 사용 할 수도 있음
s = struct.Struct('cf2d')
print(s.pack(bytes('a', encoding='ascii'), 4.56, 1208494, 1200305859))
print(s.format)
print(s.size)


# 기타 포맷 관련 유용한 것들
s1 = struct.Struct('<2ps')    # < 는 리틀엔디안이라는 뜻, p 는 첫바이트가 길이를 담고 있음
co = s1.pack(b'paul working directory', b'How can i make this program')
print(co)
print(struct.unpack('<ps', co))