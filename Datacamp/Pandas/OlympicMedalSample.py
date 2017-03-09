import pandas as pd

file = r'C:\Users\user\Downloads\Summer Olympic medallists 1896 to 2008.xlsx'
df = pd.read_excel(file, 'ALL MEDALISTS', skiprows=4)

print(df.head())

# 연도별 미국 메달 수 세기
USA_edition_group = df.loc[df.NOC == 'USA'].groupby('Edition')
print(USA_edition_group['Medal'].count(), '\n')

# value_count 함수
country_medals = df['NOC'].value_counts()
print(country_medals, '\n')

# 피봇 테이블 만들기 - pivot 함수도 있는데, 이게 좀더 패러미터가 많은 함수인듯함..
counted = df.pivot_table(aggfunc='count', index='NOC', values='Athlete', columns='Medal', fill_value=0)
counted['total'] = counted.sum(axis='columns')         # 전체 칼럼 기준으로 더해서 새 칼럼 만들기
counted = counted.sort_values('total', ascending=False)
print(counted, '\n')

# 중복열 없애기 - 고유 값 보기 위해서 사용함
ev_gen = df[['Event_gender', 'Gender']].drop_duplicates()
print(ev_gen, '\n')

# 그룹핑 해서 카운팅하기
medals_by_gender = df.groupby(['Event_gender', 'Gender']).count()
print(medals_by_gender, '\n')

# 불린 시리즈로 해당 로우 찾아오기
sus = (df.Event_gender == 'W') & (df.Gender == 'Men')   # 요 가로가 중요함... 늘 헷갈려
print(df[sus], '\n')

# nunique - 유일한 카테고리숫자를 보여줌
country_group = df.groupby('NOC')
Nsport = country_group.Sport.nunique()
print(Nsport.sort_values(), '\n')

# 냉전시대 미국과 러시아 경쟁상황 살펴보기
during_cold_war = (df.Edition >= 1952) & (df.Edition <= 1988)       # 마스크 하나 만들기
is_usa_urs = df.NOC.isin(['USA', 'URS'])                            # 두번째 마스크 isin 함수의 경우 여러군데 쓸 수 있음
cold_war_medal = df.loc[during_cold_war & is_usa_urs].groupby('NOC')
print(cold_war_medal.Sport.nunique(), '\n')

# 냉전기간 중 어떤 나라가 더 많이 이겼나 보는 방법
medals_won_by_country = df.pivot_table(index='Edition', columns='NOC', values='Athlete', aggfunc='count')
medal_compare = medals_won_by_country.loc[1952:1988, ['USA', 'URS']]
print(medal_compare, '\n')

most_medal = medal_compare.idxmax(axis='columns')        # idxmax 함수 쓰게 되면 해당 칼럼 값 비교 해서 가장 높은 칼럼명을 값으로 반환함
print(most_medal, '\n')
print(most_medal.value_counts())

# USA 메달 라인 플롯
df.Medal = pd.Categorical(values=df.Medal, categories=['Gold', 'Silver', 'Bronze'], ordered=True)      # 요렇게 해주면 차트 뜰 때 카테코기 순서 대로 표시해줌
usa = df.loc[df.NOC == 'USA']
usa_medal_by_year = usa.groupby(['Edition', 'Medal'])['Athlete'].count()
print(usa_medal_by_year, '\n')

usa_medal_by_year = usa_medal_by_year.unstack(level='Medal')            # 메달 칼럼을 행으로 바꾸기 위한방법임 ㅎ
print(usa_medal_by_year, '\n')

from matplotlib import pyplot as plt
usa_medal_by_year.plot()
plt.show()

# 영억 차트
usa_medal_by_year.plot.area()
plt.show()

