from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


def pdbase_home(request):
    counts = {
    'num_pdbs':Pdb.objects.count(),
    'num_chains': Chain.objects.count(),
    'num_residues': Residue.objects.count(),
    'num_atoms': Atom.objects.count()}
    return render(request, 'pdbase/pdbase_home.html',counts)

def proba(request):
    return render(request, 'pdbase/proba.html')

class Structures(ListView):
    model = Pdb
    template_name = "pdbase/structures.html"
    context_object_name = "pdbs"

class Structure(DetailView):
    model = Pdb
    template_name = "pdbase/structure.html"
    context_object_name = "pdb"

def structure_chains(request,code):
    pdb = Pdb.objects.get(pk=code)
    return render(request, 'pdbase/structure_chains.html', {'pdb':pdb})

def chain_view(request,code,chainid):
    pdb = Pdb.objects.get(pk=code)
    chain = pdb.chains.get(chain_id=chainid)
    return render(request, 'pdbase/chain_view.html', {'chain':chain,'pdb':pdb})

def residue_view(request,code,chainid,resnum):
    from scipy.spatial import cKDTree
    import numpy as np
    
    pdb = Pdb.objects.get(pk=code)
    chain = pdb.chains.get(chain_id=chainid)
    residue = chain.residues.get(num=resnum)
    all_atoms = Atom.objects.filter(residue__chain__pdb = pdb)
    atoms = residue.atoms.all()

    coords = np.array([[a.x, a.y, a.z] for a in all_atoms])
    tree = cKDTree(coords)
    distances, contacts = tree.query(coords,k=10, distance_upper_bound=5)
    atom_nums_residue = [a.num for a in atoms]  
    
    d = {}
    self_contacts = {}
    for i in atom_nums_residue: 
        a = atoms.get(num=i)
        l = [all_atoms.get(num=j+1) for j in contacts[i-1,1:]] # Bug was here!!! num=j+1 instead num=j fixes it!
        z = list(zip(l, distances[i-1, 1:])) 
        for jj in range(len(z)):
            if not l[jj] in atoms:
                d.setdefault(a,[]).append(z[jj])
            else:
                self_contacts.setdefault(a,[]).append(z[jj])

    return render(request, 'pdbase/residue_view.html', {'chain':chain,
                                                        'pdb':pdb,
                                                        'residue':residue,
                                                        'atoms':atoms,
                                                        'd':d,                                                       
                                                        'self_contacts':self_contacts,                                                       
                                                        })
