from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource

import random
import pickle

resnames = 6 * ['MET', 'THR', 'PRO', 'HID', 'ILE', 'ASN', 'ALA', 'LYS', 'ILE', 'GLY', 'ASP', 'PHE', 'TYR', 'PRO', 'GLN', 'CYS', 'LEU', 'LEU', 'CYS', 'GLY', 'ASP', 'PRO', 'LEU', 'ARG', 'VAL', 'SER', 'TYR', 'ILE', 'ALA', 'LYS', 'LYS', 'PHE', 'LEU', 'GLN', 'ASP', 'ALA', 'LYS', 'GLU', 'ILE', 'THR', 'ASN', 'VAL', 'ARG', 'ASN', 'MET', 'LEU', 'GLY', 'PHE', 'SER', 'GLY', 'LYS', 'TYR', 'LYS', 'GLY', 'ARG', 'GLY', 'ILE', 'SER', 'LEU', 'MET', 'GLY', 'HID', 'GLY', 'MET', 'GLY', 'ILE', 'ALA', 'SER', 'CYS', 'THR', 'ILE', 'TYR', 'VAL', 'THR', 'GLU', 'LEU', 'ILE', 'LYS', 'THR', 'TYR', 'GLN', 'VAL', 'LYS', 'GLU', 'LEU', 'LEU', 'ARG', 'ILE', 'GLY', 'THR', 'CYS', 'GLY', 'ALA', 'ILE', 'SER', 'PRO', 'LYS', 'VAL', 'GLY', 'LEU', 'LYS', 'ASP', 'ILE', 'ILE', 'MET', 'ALA', 'THR', 'GLY', 'ALA', 'SER', 'THR', 'ASP', 'SER', 'LYS', 'THR', 'ASN', 'ARG', 'VAL', 'ARG', 'PHE', 'LEU', 'ASN', 'HIE', 'ASP', 'LEU', 'SER', 'ALA', 'THR', 'PRO', 'ASP', 'PHE', 'GLU', 'LEU', 'SER', 'LEU', 'ARG', 'ALA', 'TYR', 'GLN', 'THR', 'ALA', 'LYS', 'ARG', 'LEU', 'GLY', 'ILE', 'ASP', 'LEU', 'LYS', 'VAL', 'GLY', 'ASN', 'VAL', 'PHE', 'SER', 'SER', 'ASP', 'PHE', 'PHE', 'TYR', 'SER', 'PHE', 'GLU', 'THR', 'HIE', 'ALA', 'PHE', 'ASP', 'LEU', 'MET', 'ALA', 'LYS', 'TYR', 'ASN', 'HID', 'LEU', 'ALA', 'ILE', 'GLU', 'MET', 'GLU', 'ALA', 'ALA', 'GLY', 'LEU', 'TYR', 'ALA', 'THR', 'ALA', 'MET', 'GLU', 'LEU', 'ASN', 'ALA', 'LYS', 'ALA', 'LEU', 'CYS', 'LEU', 'CYS', 'SER', 'VAL', 'SER', 'ASP', 'HIE', 'LEU', 'ILE', 'THR', 'LYS', 'GLU', 'ALA', 'LEU', 'SER', 'PRO', 'LYS', 'GLU', 'ARG', 'VAL', 'GLU', 'SER', 'PHE', 'ASP', 'ASN', 'MET', 'ILE', 'ILE', 'LEU', 'ALA', 'LEU', 'GLU', 'MET', 'MET', 'SER']

def num_to_res(n):
    chains = list('ABCDEF')
    chain = chains[(n-1)//233]
    resname = resnames[n-1]
    return u"%s %s %s" %(resname,chain,n%233 or 233)


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

def correlations(request,pk,num=1):
    corr = pickle.load(open('/mnt/supermicro/avocado/%s/correlations.pkl' %pk,'rb'))
    phi = '\u03c6'
    psi = '\u03c8'
    n = int(num)
    phi_res = corr.get((n,phi),{})
    psi_res = corr.get((n,psi),{})
    phi_res = dict(sorted(phi_res.items(),key=lambda x: x[1], reverse=True))
    psi_res = dict(sorted(psi_res.items(),key=lambda x: x[1], reverse=True))
    trajectory =  MDtrajectory.objects.get(id=pk)
    return render(request,'md/correlations.html' , 
                        {'trajectory': trajectory, 
                          'num':num,
                          'residue':num_to_res(n),
                          'phi_res':phi_res,
                          'psi_res':psi_res,
                          'prev':int(num)-1,
                          'next':int(num)+1,
                            })

def overlap(request,pk,num1,num2):
    n1 = int(num1)
    n2 = int(num2)
    trajectory =  MDtrajectory.objects.get(id=pk)
    return render(request,'md/overlap.html' , 
                        {'trajectory': trajectory, 
                          'residue1':num_to_res(n1),
                          'residue2':num_to_res(n2),
                          'num1':n1,
                          'num2':n2,
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
