from detection import data_frame
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

cds = ColumnDataSource(data_frame)

p = figure(x_axis_type="datetime", height=100, width=200,sizing_mode="scale_width",title="Motion Graph")
p.yaxis.minor_tick_line_color = None

hover = HoverTool(
    tooltips = [
        ("Start", "@Start{%d/%m/%Y %H:%M:%S}"), 
        ("End", "@End{%d/%m/%Y %H:%M:%S}")
    ],
    formatters = {
        "@Start" : "datetime",
        "@End" : "datetime"
    }
)

p.add_tools(hover)

q = p.quad(left="Start", right="End", bottom=0, top=1, color="Pink", source=cds)

output_file("Graph1.html")
show(p)
