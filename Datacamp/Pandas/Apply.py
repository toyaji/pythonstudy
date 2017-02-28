import pandas as pd
import os.path
import h5py
import numpy as np

hdf = '~user\\Downloads\\L-L1_LOSC_4_V1-931110912-4096.hdf5'
path = os.path.expanduser(hdf)


# hdf5 파일 안에 살펴보기
df = h5py.File(path, 'r')
for i in df.items():
    print(i)

# 그룹 따라 들어가서 데이터셋 찾기
group = df['quality/simple']
print([x for x in group.items()])

# 데이터 셋 넌파아어레이로 전환
dataset = np.array(group['DQmask'])
result = pd.DataFrame(dataset)

print(result.head())

# for 문 없이도 판다스를 이용해서 데이터 프레임에 함수 적용할 수 있음
def to_nonzero(x):
    # todo define color
    return x + 4 # np.random.randint(1, 10)

# 이게 랜덤이 각각 적용되는건 아니구나... 함수는 한번 돌리고 한번에 다 적용하는 거임...
result[1] = result[[0]].apply(to_nonzero)
print(result.loc[result[0] > 0, :])

# 키 넣어서 맵핑 객체 넣기
dic = {
    130803: 'Big',
    131075: 'MoreBig'
}
result['Size'] = result[1].map(dic)
print(result.loc[result[0] > 0, :])