from os.path import expanduser
import pandas as pd
from bokeh.charts import Bar
from bokeh.io import curdoc, output_file, show
from bokeh.layouts import widgetbox
from bokeh.models import Slider, HoverTool, ColumnDataSource
from bokeh.plotting import figure



def data_settting(data, year='1980'):
    plot = figure(title='Agriculture Employment on 1980', plot_height=400, plot_width=700)
    plot.vbar(x='Region', bottom=0, source=data, top=year, width=0.5)

    plot.xaxis.axis_label = 'Continents'
    plot.yaxis.axis_label = 'Employment (%)'

    show(plot)

    curdoc().add_root(plot)
    curdoc().title = 'Agriculture Employment'



if __name__ == '__main__':
    file = expanduser(r'~\documents\clean.csv')
    df = pd.read_csv(file)
    data = df.dropna()

    data_settting(data)

