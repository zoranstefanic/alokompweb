from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource

from numpy import pi
import numpy as np
import pandas as pd
import pickle

def plot_rmsd(request):
    df = pd.read_csv('/mnt/supermicro/disk1/MD/PNP/5lu0_po4/hexamer/amber/R02/5lu0_PO4_torsion-chainF.dat', delim_whitespace=True)
    p = figure(width=1500,tools="wheel_zoom,box_zoom,reset",)
    p.line(x=df.index, y=df.iloc[:,1], line_width=0.5)
    script, div = components(p)

    return render(request, 'plots/bokeh_plot.html' , {'script': script, 'div':div})

def plot_torsion(request):
    df = pd.read_csv('/mnt/supermicro/disk1/MD/PNP/5lu0_po4/hexamer/amber/R02/5lu0_PO4_torsion-chainF.dat', delim_whitespace=True)
    #df = pd.DataFrame(np.random.randn(100))
    p = figure(width=1500,tools="wheel_zoom,box_zoom,reset",)#y_range=(0,5))
    #p.grid.visible = True
    p.line(x=df.index, y=df.iloc[:,1], line_width=0.5)
    script, div = components(p)

    return render(request, 'plots/bokeh_plot.html' , {'script': script, 'div':div})

def plot_qscore(request):
    df = pickle.load(open('/home/nginx/alokompweb/alignments/q.pkl','rb'))
    p = figure(tools="wheel_zoom,box_zoom,reset",)
    p.rect(source =ColumnDataSource(df),x="Cmoving",y="Cfixed")

    script, div = components(p)

    return render(request, 'plots/bokeh_plot.html' , {'script': script, 'div':div})

def bokeh_plot(request):
    n = 5000
    x = 2 + 2*np.random.standard_normal(n)
    y = 2 + 5*np.random.standard_normal(n)

    p = figure(width=1000,height=1000,title="Hexbin for 500 points", match_aspect=True,
               tools="wheel_zoom,reset", background_fill_color='#440154')
    p.grid.visible = True

    r, bins = p.hexbin(x, y, size=0.5, hover_color="pink", hover_alpha=0.8)

    #p.circle(x, y, color="white", size=2)

    p.add_tools(HoverTool(
        tooltips=[("count", "@c"), ("(q,r)", "(@q, @r)")],
        mode="mouse", point_policy="follow_mouse", renderers=[r]
    ))
    script, div = components(p)

    return render(request, 'plots/bokeh_plot.html' , {'script': script, 'div':div})

