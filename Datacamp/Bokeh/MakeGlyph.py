from os.path import expanduser
from bokeh.plotting import figure, output_file, show
import pandas as pd


file = expanduser(r'~\Downloads\TREND01-5G-educ-fertility-bubbles.xls')
df = pd.read_excel(file, 'data COMPILATION', skiprows=7, skip_footer=20)

# 그룹핑 해서 나눠놓기
fertility_africa = df[df['Continent'] == 'AF'].fertility
fertility_latin = df[df['Continent'] == 'LAT'].fertility
female_literacy_africa = df[df['Continent'] == 'AF']['female literacy']
female_literacy_latin = df[df['Continent'] == 'LAT']['female literacy']


p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')
p.circle(fertility_latin, female_literacy_latin, color='Aquamarine', size=8, alpha=0.6)
p.x(fertility_africa, female_literacy_africa, color='CadetBlue', size=8, alpha=0.6)

output_file('fert_lit.html')
show(p)