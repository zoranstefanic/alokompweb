from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from .models import *
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource

import random
import networkx as nx
import pickle
import matplotlib.pyplot as plt
import io
import base64
import numpy as np
import json

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

class CorrelationMatrixView(DetailView):
    model = MDtrajectory
    context_object_name = 'trajectory'
    template_name = "md/correlation_matrix.html"

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

def residue_in_all(request,trid,resid):
    this =  MDtrajectory.objects.get(id=trid)
    traj_list = [t.id for t in MDtrajectory.objects.exclude(torsions=None)]
    return render(request, 'md/residue_in_all.html', 
                       { 
                        'trajectory':this,
                        'traj_list':traj_list,
                        'num':resid,
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
    corr = pickle.load(open('/mnt/supermicro/avocado/%s/correlations_.pkl' %pk,'rb'))
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

def correlations_old(request,pk,num=1):
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

def correlations_circular(request,pk,num=1):
    corr = pickle.load(open('/mnt/supermicro/avocado/%s/correlations_c.pkl' %pk,'rb'))
    phi = '\u03c6'
    psi = '\u03c8'
    n = int(num)
    phi_res = corr.get((n,phi),{})
    psi_res = corr.get((n,psi),{})
    phi_res = dict(sorted(phi_res.items(),key=lambda x: x[1], reverse=True))
    psi_res = dict(sorted(psi_res.items(),key=lambda x: x[1], reverse=True))
    trajectory =  MDtrajectory.objects.get(id=pk)
    traj_list = [t.id for t in MDtrajectory.objects.exclude(torsions=None)]
    return render(request,'md/correlations.html' , 
                        {'trajectory': trajectory, 
                          'num':num,
                          'residue':num_to_res(n),
                          'phi_res':phi_res,
                          'psi_res':psi_res,
                          'prev':int(num)-1,
                          'next':int(num)+1,
                          'traj_list':traj_list,
                            })

def correlations_highest(request,pk,num=1):
    limit = request.GET.get('limit',None)
    corr = pickle.load(open('/mnt/supermicro/avocado/%s/correlations_c.pkl' %pk,'rb'))
    phi = '\u03c6'
    psi = '\u03c8'
    n = int(num)
    phi_res = corr.get((n,phi),{})
    psi_res = corr.get((n,psi),{})
    phi_res = dict(sorted(phi_res.items(),key=lambda x: x[1], reverse=True))
    psi_res = dict(sorted(psi_res.items(),key=lambda x: x[1], reverse=True))
    if limit:
        phi_res = {k:v for k,v in phi_res.items() if abs(v) > float(limit)}
        psi_res = {k:v for k,v in phi_res.items() if abs(v) > float(limit)}
    trajectory =  MDtrajectory.objects.get(id=pk)
    traj_list = [t.id for t in MDtrajectory.objects.exclude(torsions=None)]
    return render(request,'md/correlations_highest.html' , 
                        {'trajectory': trajectory, 
                          'num':num,
                          'residue':num_to_res(n),
                          'phi_res':phi_res,
                          'psi_res':psi_res,
                          'prev':int(num)-1,
                          'next':int(num)+1,
                          'traj_list':traj_list,
                          'limit':limit,
                            })

def correlations_for_traj(request,pk):
    limit = float(request.GET.get('limit',0.5))
    trajectory =  MDtrajectory.objects.get(id=pk)
    corr = pickle.load(open('/mnt/supermicro/avocado/%s/correlations_c.pkl' %pk,'rb'))
    traj_list = [t.id for t in MDtrajectory.objects.exclude(torsions=None)]
    correlations = []
    for k in corr.keys():
        for kk in corr[k].keys():
            if abs(corr[k][kk]) > limit:
                correlations.append((k,kk,corr[k][kk])) 
    l = []
    for k in correlations:
        if (k[1],k[0],k[2]) not in l:
            l += k,
    correlations = sorted(l, key=lambda x: abs(x[2]), reverse=True)
    return render(request,'md/correlations_for_traj.html' , 
                        {'trajectory': trajectory, 
                          'traj_list':traj_list,
                          'limit':limit,
                          'corr':correlations,
                            })

def avocados(request,pk,chain):
    trajectory =  MDtrajectory.objects.get(id=pk)
    #imgmap =  {n:[(n-1)//18+1, n%18 or 18] for n in range(1,234)} # for the old style imagemaps
    imgmap =  {n:[(n-1)//16+1, n%16 or 16] for n in range(1,234)}
    d = {}
    offset = dict(zip(list('ABCDEF'),[i*233 for i in range(6)]))[chain]
    for k,v in imgmap.items():
        i,j = v[0],v[1]
        d[k+offset] = [(j-1)*100,(i-1)*100,j*100,i*100]
    return render(request,'md/avocados.html' , 
                        {'trajectory': trajectory, 
                          'imgmap':d,
                          'chain':chain,
                          'offset':offset,
                            })

def avocados_active_site(request,pk,chain):
    D1_nums = '19,20,21,23,24,64,87,89,90,160,180,203,214,215,217,218,221'.split(',') # Dimer 1 that makes the active site
    D2_nums = '1,2,3,4,42,43'.split(',') # Dimer 2
    # Dimers are A-D B-E C-F
    offset = dict(zip(list('ABCDEF'),[i*233 for i in range(6)]))[chain]
    nums = [int(i)+offset for i in D1_nums]
    nums += [(int(i)+233*3 + offset)%1398 for i in D2_nums]
    amino_acids = dict([(str(i),num_to_res(i)) for i in nums])
    trajectory =  MDtrajectory.objects.get(id=pk)
    imgmap =  {n:[(n-1)//18+1, n%18 or 18] for n in range(1,234)}
    d = {}
    for k,v in imgmap.items():
        i,j = v[0],v[1]
        d[k+offset] = [(j-1)*100,(i-1)*100,j*100,i*100]
    return render(request,'md/avocados_active_site.html' , 
                        {'trajectory': trajectory, 
                          'imgmap':d,
                          'chain':chain,
                          'offset':offset,
                          'nums':nums,
                          'amino_acids':amino_acids,
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

def changepoints_plot(request,id):
    changepoints = pickle.load(open('/mnt/supermicro/avocado/%s/change_points_diffs.pkl' %id,'rb'))
    x = [_[0] for _ in changepoints]
    y = [_[1] for _ in changepoints]
    r = [_[2]/5 for _ in changepoints]
    TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,help,reset"
    p = figure(tools=TOOLS,width=1200,height=1200)
    p.ygrid.ticker = [233*i for i in range(6)]
    p.xgrid.ticker = [100*i for i in range(40)]
    p.scatter(x,y,radius=r,fill_alpha=0.5,line_color=None,)
    script, div = components(p)
    traj_list = [t.id for t in MDtrajectory.objects.exclude(torsions=None)]
    return render(request, 'md/changepoints_plot.html' , {'script': script, 'div':div, 'id':id, 'traj_list':traj_list })

def residue_position_on_unit_circle(n,phi):
    #    A  F
    #  D      C
    #    B  E
    CA_distances = pickle.load(open('/mnt/supermicro/avocado/CA_centar_distances.pkl', 'rb'))
    angle_offsets_dict = {'A': 90, 'B': 210, 'C': 330, 'D': 150, 'E': 270, 'F': 30}
    if phi == 'φ':offset = 60/(233*3)
    else:offset = 120/(233*3)
    chain = list('ABCDEF')[(n-1)//233]
    angle = angle_offsets_dict[chain] + 60*((n-1)%233)/233 + offset
    angle_radians = np.radians(angle)
    r = CA_distances[n-1]
    return r*np.cos(angle_radians), r*np.sin(angle_radians)

def graph_plot(request,id):
    traj_list = [t.id for t in MDtrajectory.objects.exclude(torsions=None)]
    plt.cla()
    pie = plt.pie([60]*6,startangle=90,labels=['A','D','B','E','C','F'])
    for w in pie[0]:
        w.set_alpha(0.2)
    dpi = request.GET.get('dpi',None)
    core = request.GET.get('core',None)
    if dpi:
        dpi = int(dpi)
    cm = pickle.load(open('/mnt/supermicro/avocado/%s/correlations_c.pkl' %id,'rb'))
    G = nx.Graph()
    G.add_weighted_edges_from({(k,v,cm[k][v]) for k in cm.keys() for v in cm[k]})
    if core:
        G = nx.k_core(G,int(core))
    bc = list(nx.betweenness_centrality(G,weight="weight").values())
    wghts = [G[k][v]['weight'] for k,v in G.edges]
    pos = {n:residue_position_on_unit_circle(*n) for n in G.nodes}
    degrees = [nx.degree(G,k)*5 for k in G.nodes]
    nx.draw_networkx(G, pos=pos, node_color=degrees, node_size=degrees, font_size=2, width=0.3, edge_color=wghts, edge_cmap=plt.cm.RdBu, edge_vmax=1, edge_vmin=-1, alpha=0.8)
    img = io.BytesIO()
    plt.savefig(img,dpi=dpi or 1000,bbox_inches='tight',pad_inches=0)
    plot = base64.b64encode(img.getvalue()).decode()
    return render(request, 'md/graph.html' , {'plot': plot,'id':id, 'core':core,'traj_list':traj_list})

def d3plot(request):
    return render(request, 'md/corr.html' , {'traj_id': 1458 })

# Correlations 
def coords(request):
    coords = json.load(open('/mnt/supermicro/disk1/ALOKOMP/hexamer.json','r'))
    return JsonResponse(coords)

def corr(request,traj_id):
    corr = json.load(open('/mnt/supermicro/avocado/%s/correlations.json' %traj_id,'r'))
    return JsonResponse(corr,safe=False)

def corrd3(request,traj_id):
    trajectories = '1184 1192 1234 1242 1306 1314 1458 1643 1651 1659 1697 1706 1714 1717 1725 1733 1745 1753 1761 1807 1815 1821 1831 1839'.split()
    return render(request, 'md/corr.html' , {'traj_id': traj_id, 'trajectories':trajectories })

def corrd3_all(request,traj_id):
    trajectories = '1184 1192 1234 1242 1306 1314 1458 1643 1651 1659 1697 1706 1714 1717 1725 1733 1745 1753 1761 1807 1815 1821 1831 1839'.split()
    corr = json.load(open('/mnt/supermicro/avocado/%s/correlations.json' %traj_id,'r'))
    all_correlated = list(set([s['source'] for s in corr]))
    hubs = {}
    for r in corr:
        k = r['source']
        if k in hubs.keys():
            hubs[k] +=1
        else:
            hubs.setdefault(k,1)
    #hubs = {i:hubs.setdefault(i,0) for i in range(1,1399)}
    return render(request, 'md/corrd3_all.html',
            {'traj_id': traj_id, 
            'all_correlated': all_correlated,  
            'trajectories':trajectories, 
            'hubs':hubs, 
            })

# Janin related views 
def janins(request,pk):
    trajectory =  MDtrajectory.objects.get(id=pk)
    return render(request,'md/janins.html' , {'trajectory': trajectory, })

def janin(request,pk,chain):
    "One chain Janin plots montage"
    trajectory =  MDtrajectory.objects.get(id=pk)
    imgmap =  {n:[(n-1)//14+1, n%14 or 14] for n in range(1,144)}
    d = {}
    offset = dict(zip(list('ABCDEF'),[i*144 for i in range(6)]))[chain]
    for k,v in imgmap.items():
        i,j = v[0],v[1]
        d[k+offset] = [(j-1)*100,(i-1)*100,j*100,i*100]
    return render(request,'md/janin.html' , 
                        {'trajectory': trajectory, 
                          'imgmap':d,
                          'chain':chain,
                          'offset':d,
                            })

def janin_json(request,traj_id):
    corr = json.load(open('/mnt/supermicro/avocado/%s/janin_corr.json' %traj_id,'r'))
    return JsonResponse(corr,safe=False)

def janin_corr(request,traj_id):
    trajectories = '1184 1192 1234 1242 1306 1458 1643 1651 1659 1697 1706 1714 1717 1725 1733 1745 1753 1761 1807 1815 1821 1831 1839'.split()
    return render(request, 'md/janin_corr.html' , {'traj_id': traj_id, 'trajectories':trajectories })

# Changepoints 
def changepoints(request,traj_id):
    trajectories = '1184 1192 1234 1242 1306 1314 1458 1643 1651 1659 1697 1706 1714 1717 1725 1733 1745 1753 1761 1807 1815 1821 1831 1839'.split()
    neighbours = json.load(open('/mnt/supermicro/avocado/neighbours15.json','r'))
    corr = json.load(open('/mnt/supermicro/avocado/%s/correlations.json' %traj_id,'r'))
    cpts = json.load(open('/mnt/supermicro/avocado/%s/changepoints_%s.json' %(traj_id,traj_id),'r'))
    all_correlated = list(set([s['source'] for s in corr]))
    cpts_by_number = {k['aa']:len(k['cpts']) for k in cpts}
    return render(request, 'md/changepoints.html',
            {'traj_id': traj_id, 
            'all_correlated': all_correlated,  
            'cpts': cpts,  
            'trajectories':trajectories, 
            'cpts_by_number':cpts_by_number, 
            'neighbours':neighbours, 
            })

# Temporal paths
def paths(request,traj_id):
    trajectories = '1184 1192 1234 1242 1306 1314 1458 1643 1651 1659 1697 1706 1714 1717 1725 1733 1745 1753 1761 1807 1815 1821 1831 1839'.split()
    paths = json.load(open('/mnt/supermicro/avocado/%s/filterd_dijkstra_paths_%s.json' %(traj_id,traj_id),'r'))
    return render(request, 'md/paths.html',
            {'traj_id': traj_id, 
            'trajectories':trajectories, 
            'paths':paths, 
            })

def paths_view(request,traj_id,n):
    trajectories = '1184 1192 1234 1242 1306 1314 1458 1643 1651 1659 1697 1706 1714 1717 1725 1733 1745 1753 1761 1807 1815 1821 1831 1839'.split()
    paths = json.load(open('/mnt/supermicro/avocado/%s/filterd_dijkstra_paths_%s.json' %(traj_id,traj_id),'r'))
    paths = sorted(paths,key=lambda a: len(a[0]),reverse=True)
    total = len(paths)
    paths = paths[:int(n)]
    return render(request, 'md/paths_view.html',
            {'traj_id': traj_id, 
            'trajectories':trajectories, 
            'paths':paths, 
            'total':total, 
            })
