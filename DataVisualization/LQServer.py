from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.plotting import ColumnDataSource, Figure, show
from bokeh.models.widgets import Select, TableColumn, DataTable, Div, Paragraph
from bokeh.models import HoverTool, ContinuousTicker, WidgetBox
import pandas as pd
from bokeh.palettes import Paired8, Category20
from collections import defaultdict

df = pd.read_csv('LQ.csv', engine='python')

def ranktrim(df):
    tf = df.groupby(['year', 'crop']).sum().reset_index()

    db = {}
    cums = {}
    for y in tf.year.unique().tolist():
         tt = tf[tf.year == y].sort_values(['area'], ascending=False)
         tt['cumulative_area'] = tt.area.cumsum() / tt.area.sum()
         db[str(y)] = tt.crop[:10].values
         cums[str(y)] = tt.cumulative_area[:10].values
    top10 = pd.DataFrame(db)
    db = ColumnDataSource(data=db)
    cum = (pd.DataFrame(cums)[9:]*100).round(2)
    cum = ColumnDataSource(data=cum)
    
    # 작물별로 매해 rank 변화 점수화하기
    rankcollection = defaultdict(list)
    for crop in ['배추', '감자', '옥수수', '논벼', '당근', '무', '고추', '양배추', '콩', '양파', '팥', '들깨', '파', '메밀']:
        for colum in top10.columns:
            if crop in top10[colum].tolist():
                index = top10[colum].tolist().index(crop)
                rankcollection[crop].append(10 - index)
            else:
                rankcollection[crop].append(0)

    return db, cum, rankcollection


def get_data(choosen):
    """
    DataFrame 을 Bokeh ColumdataSource 로 쓸 수 있는 딕셔너리로 전환해주는 함수
    :param choosen: 해당 작물을 변수로 넘겨주면 찍어서 가공해줌
    :return: 딕셔너리로
    """
    tf = df[df.crop == choosen]
    regions = df.region.unique().tolist()
    year = list((tf[tf.region == r]['year'] for r in regions))
    area = list((tf[tf.region == r]['area'] for r in regions))
    product = list((tf[tf.region == r]['production'] for r in regions))
    areaLQ = list((tf[tf.region == r]['areaLQ'] for r in regions))
    productionLQ = list((tf[tf.region == r]['productionLQ'] for r in regions))
    color = Paired8
    return {'year': year, 'area': area, 'product': product, 'areaLQ': areaLQ, 'productionLQ': productionLQ, 'region': regions, 'color': color}

def get_data_raw(choosen):
    tf = df[df.crop == choosen]
    return {'year': tf.year, 'area': tf.area, 'region': tf.region}


#
source = ColumnDataSource(data=get_data('감자'))

# figure 생성부
p1 = Figure(plot_height=300, plot_width=1000, x_axis_label='Year', y_axis_label='Area', toolbar_location='above', title='작물별 재배면적 시계열')
p1.multi_line('year', 'area', alpha=1, color='color', legend='region', source=source)
p2 = Figure(plot_height=300, plot_width=1000, x_axis_label='Year', y_axis_label='Production', toolbar_location='above', title='작물별 생산량 시계열')
p2.multi_line('year', 'product', alpha=1, color='color', legend='region', source=source)
p3 = Figure(plot_height=300, plot_width=1000, x_axis_label='Year', y_axis_label='AreaLQ', toolbar_location='above', title='면적기준 LQ 시계열')
p3.multi_line('year', 'areaLQ', alpha=1, color='color', legend='region', source=source)
p4 = Figure(plot_height=300, plot_width=1000, x_axis_label='Year', y_axis_label='ProductionLQ', toolbar_location='above', title='생산량기준 LQ 시계열')
p4.multi_line('year', 'productionLQ', alpha=1, color='color', legend='region', source=source)

# 통합 디자인 부분임
for f in [p1, p2, p3, p4]:
    f.add_tools(HoverTool(line_policy='next', tooltips=[('Region', '@region')], ))
    f.legend.orientation = "horizontal"
    f.legend.background_fill_alpha = 0.2

crops = df.crop.unique().tolist()

# 작물 연도별 순위 데이터 보여주는 데이터 칼럼 보기
titlediv = Div(text="""<h1>연도별 재배면적 상위 10개 작물</h1>""", width=1000)
db, cum, rank = ranktrim(df)
columns = [TableColumn(field=c, title=c) for c in db.column_names]
data_table = DataTable(source=db, columns=columns, height=300, width=1000)
cums_table = DataTable(source=cum, columns=columns, height=70, width=1000)
para = Paragraph(text="""상위 10개 종목의 평창군 전체 재배면적 대비 누적 면적(%)""", height=25, width=1000)

# rank chart 그리는 부분임
ranksource = ColumnDataSource(data={'crop': list(rank.keys()), 'rank': list(rank.values()), 'year': [db.column_names] * len(rank), 'color': Category20[14]})
p = Figure(plot_width=1000, plot_height=300, x_axis_label='Year', y_axis_label='Rank', toolbar_location='above', title='재배면적 상위 10개종목 순위변화')
p.multi_line('year', 'rank', alpha=1, color='color', source=ranksource)
p.add_tools(HoverTool(tooltips=[('Crop', '@crop')]))

# 작물 select 하면 맞춰서 그래프 움직이는 부분
select = Select(title="Crop", value="감자", options=crops)

def update_crop(attr, old, new):

    source.data = get_data(str(select.value))

select.on_change('value', update_crop)

seconddiv = Div(text="""<h1>읍면동별 작물 시계열 차트</h1>""", width=1000)


rankwidget = WidgetBox(titlediv, data_table, para, cums_table)
chartwidget = WidgetBox(seconddiv, select)
layout = column(rankwidget, p, chartwidget, p1, p2, p3, p4)
curdoc().add_root(layout)
