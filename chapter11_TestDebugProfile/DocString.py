# 문서화 문자열을 잘 정리해주고 수정될대마다 업데이트 해줘야 사용자가 문제생기면 찾기편리함

def split(line, types=None, delimeter=None):
    """텍스트 줄을 분할하고 추가적으로 타입 변환을 수행한다.
        예를 들어:

        >>> split('GOOG 100 490.50')
        ['GOOG', '100', '490.50']
        >>> split('GOOG 100 490.50', [str, int, float])
        ['GOOG', 100, 490.5]

        기본으로 공백을 기준을 분할되지만 delimiter 키워드 인수를 통해
        다른 구분자를 선택할 수도 있다.

        >>> split('GOOG,100,490.50', delimeter=',')
        ['GOOG', '100', '490.50']
        >>>
    """
    fields = line.split(delimeter)
    if types:
        fields = [ty(val) for ty, val in zip(types, fields)]
    return fields