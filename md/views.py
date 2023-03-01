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

class MDAnalyzedView(ListView):
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

def residue_in_replicas(request,trid,resid):
    this =  MDtrajectory.objects.get(id=trid)
    img_list = [i for i in range(10)]
    trajectories =  MDtrajectory.objects.filter(file__endswith=this.filename())
    return render(request, 'md/residue_in_replicas.html', 
                        {'trajectories': trajectories,
                        'img_list':img_list,
                        'resid':resid,
                         'prev':int(resid)-1,
                         'next':int(resid)+1,
                         }
                  )

def ramachandran(request,pk,num=1):
    trajectory =  MDtrajectory.objects.get(id=pk)
    img_list = [i for i in range(10)]
    return render(request, 'md/ramachandran.html' , 
                        {'trajectory': trajectory, 
                          'img_list':img_list,
                          'num':num,
                          'prev':int(num)-1,
                          'next':int(num)+1,
                            })

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
