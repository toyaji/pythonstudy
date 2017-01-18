prices = {
    "goog" : 2204.10,
    "SCOX" : 293.1
}

if "SCOX" in prices:
    p = prices["SCOX"]
else:
    p = 0.0


p = prices.get("SCOX", 0.0)  # 위에 if 구문 짧게 쓰는방법