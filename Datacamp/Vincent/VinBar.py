import vincent
import pandas_datareader as pdr
import pandas as pd
from datetime import datetime

start = datetime(2010, 1, 1)
end = datetime(2017, 2, 11)
stock = pdr.DataReader("078930.KS", "yahoo", start, end)

df = pd.DataFrame(stock)

#
vincent.core.initialize_notebook()

# 빈센트로 바차트 오브젝트 만들어줌
bar = vincent.Bar(df['High'])

bar.display()