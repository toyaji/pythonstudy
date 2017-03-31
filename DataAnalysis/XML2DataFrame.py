import requests
from lxml.html import parse
from io import StringIO

text = requests.get('http://finance.yahoo.com/quote/AAPL/options?ltr=1').text
parsed = parse(StringIO(text))

doc = parsed.getroot()

print(doc)