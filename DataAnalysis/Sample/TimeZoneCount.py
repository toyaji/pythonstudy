import json

path = r'C:\Users\user\Downloads\DataDownload\usagov_bitly_data.txt'

# json 읽어서 딕셔너리로 구성해줌
records = [json.loads(line) for line in open(path, encoding='UTF-8')]

# 타임존 보기
print(records[0]['tz'])

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zones)

# 타임존 세는 함수
from collections import defaultdict  # defaultdict 하면 기본적으로 키값 없어서 해당 오브젝트로 딕트구성함


def get_count(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts


count = get_count(time_zones)
print(count['Asia/Seoul'])


# 탑 10 알고 싶을때
def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]


print(top_counts(count))

# 더 쉬운 방법
from collections import Counter

counter = Counter(time_zones)  #
print(counter.most_common(10))

# 데이터 프레임 만들기
import pandas as pd

frame = pd.DataFrame(records)
print(frame.info())

# 카운팅해서 순서대로 열개만 보기
tz_counts = frame['tz'].value_counts()
print(tz_counts[:10], '\n')

# 공백 채워서 데이터 정리하기
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print(tz_counts[:10], '\n')

# 플롯 그리기
import matplotlib.pyplot as plt

tz_counts[:10].plot(kind='barh', rot=0)
plt.show()

# 브라우저 토큰 잘라내기
results = pd.Series([x.split()[0] for x in frame.a.dropna()])   # 해당 칼럼에서 값 없는 놈 떨구고 시리즈 만들기
print(results[:5])
print(results.value_counts()[:8])

# 윈도우 사용자 걸러내기
cframe = frame[frame.a.notnull()]

import numpy as np

operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Now Windows')  # 뒤에는 있으면 줄값, 없으면 줄값
print(operating_system[:5])

# 데이터 그룹 묶기
by_tz_os = cframe.groupby(['tz', operating_system])


# 그룹별 함수 size() 로 카운팅 가능함
agg_counts = by_tz_os.size().unstack().fillna(0)
print(agg_counts[:10])

# 전체 표준 시간대 순위 보기
indexer = agg_counts.sum(1).argsort()    # sum 안에 숫자는 axis / argsort() 하면 그 자리에 대체하고 null 값은 없애버림
print(indexer[:10])

# 위에 정렬 순서를 적용해서 다시 잘라내기
count_subnet = agg_counts.take(indexer)[-10:]
print(count_subnet)

# 중첩 그래프 만들기
count_subnet.plot(kind='barh', stacked=True)
plt.show()

# 각 행의 총합을 1로 정규화해서 비율 확인하기
normed_subset = count_subnet.div(count_subnet.sum(1), axis=0)   # .div 주어진 인자값으로 나누는 함수
normed_subset.plot(kind='barh', stacked=True)
plt.show()