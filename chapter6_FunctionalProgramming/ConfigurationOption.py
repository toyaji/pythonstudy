def make_table(data, **parms):
    fgcolor = parms.pop("fgcolor", "black")
    bgcolor = parms.pop("bgcolor", "white")
    width = parms.pop("width", None)
    if parms:
        raise TypeError("Unsupported configuration options %s" % list(parms))

items = [2, 3, 4, 6]
make_table(items, fgcolor="black", bgcolor="white", width=400)

# 함수 정의할때 ** 하면 사전식으로 맨 뒤에 아이들 다 가져옴


