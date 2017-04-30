from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models import Slider
from bokeh.plotting import figure


def curod1():
    plot = figure()
    plot.line([1,2,3,4,5], [2,5,4,6,7])

    curdoc().add_root(plot)


if __name__ == '__main__':
    curod1()