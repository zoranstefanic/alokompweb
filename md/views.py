from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource

import random

class MDdirectoriesView(ListView):
    model = MDdirectory
    context_object_name = 'directories'
    template_name = "md/directories.html"

class MDtrajectoriesView(ListView):
    model = MDtrajectory
    context_object_name = 'trajectories'
    template_name = "md/trajectories.html"

class MDwithTorsionsView(ListView):
    model = MDtrajectory
    context_object_name = 'trajectories'
    template_name = "md/trajectories.html"
    
    def get_queryset(self):
        return MDtrajectory.objects.exclude(torsions=None)

class MDdirectoryView(DetailView):
    model = MDdirectory
    context_object_name = 'directory'
    template_name = "md/directory.html"

class MDtrajectoryView(DetailView):
    model = MDtrajectory
    context_object_name = 'trajectory'
    template_name = "md/trajectory.html"

def replica(request,n):
    trajectories =  MDtrajectory.objects.exclude(torsions=None).filter(replica=n)
    return render(request, 'md/trajectories.html' , {'trajectories': trajectories, })

def torsion_plot(request,id):
    ta = TorsionAngle.objects.get(id=id)
    torsions = ta.values['torsions']
    other = random.choice(ta.trajectory.torsions.all())
    torsions1 = other.values['torsions']
    p = figure(width=2000,tools="wheel_zoom,box_zoom,reset")
    p.title = ta.name + other.name
    p.line(x=range(len(torsions)), y=torsions, line_width=0.5)
    p.line(x=range(len(torsions)), y=torsions1,color="lime",line_width=0.5)

    script, div = components(p)
    return render(request, 'md/torsion_plot.html' , {'script': script, 'div':div, 'ta':ta, 'other':other })
