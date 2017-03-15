import pandas as pd
import os
encoding = 'latin1'

upath = os.path.expanduser(r'~\Downloads\DataDownload\pydata-book-master\ch02\movielens\users.dat')
rpath = os.path.expanduser(r'~\Downloads\DataDownload\pydata-book-master\ch02\movielens\ratings.dat')
mpath = os.path.expanduser(r'~\Downloads\DataDownload\pydata-book-master\ch02\movielens\movies.dat')

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
mnames = ['movie_id', 'title', 'genres']

users = pd.read_csv(upath, sep='::', header=None, names=unames, encoding=encoding, engine='python')
ratings = pd.read_csv(rpath, sep='::', header=None, names=rnames, encoding=encoding, engine='python')
movies = pd.read_csv(mpath, sep='::', header=None, names=mnames, encoding=encoding, engine='python')

print(users.head(), '\n')
print(ratings.head(), '\n')
print(movies.head(), '\n')


# 판다스는 중복되는 열을 키값으로 테이블간 병합이 가능함
data = pd.merge(pd.merge(ratings, users), movies)
print(data.ix[0], '\n')              # ix 의 경우에 iloc 와 loc 의 기능 다 가지고 있다고 보면 됨

# 피봇 테이블로 장르별 평점 정보 수집하기
mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
print(mean_ratings.head(), '\n')

# 250 건 이상 있는 데이터만 추리기
ratings_by_title = data.groupby('title').size()
print(ratings_by_title[:10], '\n')

active_titles = ratings_by_title.index[ratings_by_title >= 250]        # 시리즈 객체로 필터값 만들기
print(active_titles, '\n')

# 위의 시리즈 인덱스 값을 마스크로 해서 추출하기
mean_ratings = mean_ratings.loc[active_titles]
print(mean_ratings, '\n')

# 여성들에게 높은 점수 받은 영화 목록 내림차순으로 정렬해서 뽑아오기
top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
print(top_female_ratings[:5], '\n')

# 평균 평점 차이 열 더하기
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_values(by='diff')
print(sorted_by_diff.head(), '\n')