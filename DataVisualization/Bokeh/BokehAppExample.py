from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models.widgets import TextInput, Button, Paragraph

button = Button(label='Say Hi')
input = TextInput(value='Bokeh')
output = Paragraph()


def update():
    output.text = "Hello, " + str(input.value)

button.on_click(update())
layout = column(button, input, output)
curdoc().add_root(layout)