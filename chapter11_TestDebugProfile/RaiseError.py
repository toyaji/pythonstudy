# 예외 처리를 적절히 사용하면 속도 향상에 도움이 됨

def parse_header(line):
    fields = line.split(":")
    if len(fields) != 2:
        raise RuntimeError("Malformed header")
    header, value = fields
    return header.lower(), value.strip()


def parse_header2(line):
    fields = line.split(':')
    try:
        header, value = fields
        return header.lower(), value.strip()
    except ValueError:
        raise RuntimeError("Malformed header")

# 자주 발생하지 않는 예외를 위해서 위에처럼 if 문 넣게 되는 경우 매번 if 문 거쳐가니까 속도가 현저히 떨어짐
# 반면에 자주 예외가 발생하는 (혹은 그런 목적으로 만드는 경우) 는 반대임. try 구문이 속도 더 오래걸림 단일 실행에서는