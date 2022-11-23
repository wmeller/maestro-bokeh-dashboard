#Imports
from datetime import datetime
from bokeh.io import show, curdoc
from bokeh.models import FileInput, Paragraph, Div, CustomJS, DatetimeRangeSlider, MultiSelect, TextInput, Button
from bokeh.layouts import gridplot, layout
from bokeh.plotting import figure, show, output_file
from bokeh.events import ButtonClick

 
def onButtonPress(event):
    print("Button Pressed!")

#Configure page settings
output_file('RSDMaestro_main.html')
curdoc().theme = 'dark_minimal'

#Define elements of dasboard
file_input = FileInput()
header = Div(text="""<h1>Remote Systems Engineering Data Dashboard - Maestro</h1>""")
p = Paragraph(text="""Your selected folder will populate the list below with all the files it finds. The date slider will filter the results by file start date.""")
datetime_range_slider = DatetimeRangeSlider(value=(datetime(2022, 3, 8, 12), datetime(2022, 3, 25, 18)), \
start=datetime(2022, 3, 1), end=datetime(2022, 3, 31))

 
datetime_range_slider.js_on_change("value", CustomJS(code="""
    console.log('datetime_range_slider: value=' + this.value, this.toString())
"""))

 
text_input = TextInput(value="default", title="Label:")
text_input.js_on_change("value", CustomJS(code="""
    console.log('text_input: value=' + this.value, this.toString())
"""))

#This should be populated with the list of files from the specified directory.
#z = [(str(index), value) for index, value in enumerate(list)] <-- this will give me what I want.

OPTIONS = [("1", "foo"), ("2", "bar"), ("3", "baz"), ("4", "quux")]
multi_select = MultiSelect(value=["1", "2"], options=OPTIONS, width=800)
multi_select.js_on_change("value", CustomJS(code="""
    console.log('multi_select: value=' + this.value, this.toString())
"""))
button = Button(label="Foo", button_type="success")
button.on_event(ButtonClick, onButtonPress)

#Define layout
dashLayout = layout([
    [header],
    [Paragraph(text="Browse for Data folder: "), file_input],
    [Paragraph(text="Search for filenames: "), text_input],
    [p],
    [datetime_range_slider],
    [multi_select],
    [button]
    ])

#Show layout
show(dashLayout, size="stretch_both")