from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from .models import *
from pdbase.models import Pdb,Residue
from alignments.models import ResidueMatch
from django.db.models import Q

def structure_symmetry(request,code):
    pdb = Pdb.objects.get(code=code)
    return render(request, 'symmetry/structure_symmetry.html', 
                    {
                    'code':code,
                    'pdb':pdb,
                    }
                )

def symmops(request):
    symmops = SymmOp.objects.all()
    return render(request, 'symmetry/symmops.html', 
                    {
                    'symmops':symmops,
                    }
                )

def symops(request):
    "New kind of symops between residues"
    symops = SymOp.objects.all()
    return render(request, 'symmetry/symops.html', 
                    {
                    'symops':symops,
                    }
                )

def symmop(request,id):
    symmop = SymmOp.objects.get(id=id)
    return render(request, 'symmetry/symmop.html', 
                    {
                   'symmop':symmop,
                    }
                )

def symop(request,id):
    symop = SymOp.objects.get(id=id)
    return render(request, 'symmetry/symop.html', 
                    {
                   'symop':symop,
                    }
                )


def residue_contact_view(request,id):
    d = {}
    rc = ResidueContact.objects.get(id=id)
    # Get all residue matches with this residue in all the alignments
    rmatches = ResidueMatch.objects.filter(fixed__in=[rc.res1,rc.res2])
    rmatches = rmatches.union(ResidueMatch.objects.filter(moving__in=[rc.res1,rc.res2])).order_by('distance') 
    return render(request, 'symmetry/residue_contact_view.html', 
                    {
                   'rc':rc,
                   'rmatches':rmatches,
                    }
                )
def residue_symmop_view(request,id):
    d = {}
    r = Residue.objects.get(id=id)
    # Get all residue matches with this residue in all the alignments
    rmatches = ResidueMatch.objects.filter(fixed=r)
    rmatches = rmatches.union(ResidueMatch.objects.filter(moving=r)).order_by('distance') 
    for rm in rmatches[:20]:
        rfi, rmo = rm.fixed, rm.moving
        #qf = Q(from_atom__residue = rfi) | Q(to_atom__residue = rfi)
        #qm = Q(from_atom__residue = rmo) | Q(to_atom__residue = rmo)
        d[(rfi,rmo)] = [rfi.contacts(),rmo.contacts()]
    return render(request, 'symmetry/residue_symmop_view.html', 
                    {
                   'r':r,
                   'rmatches':rmatches,
                   'd':d,
                    }
                )

def symmetry_gallery(request):
    pdbs = Pdb.objects.all()
    return render(request, 'symmetry/symmetry_gallery.html',{'pdbs':pdbs} )

def d3_projections(request,code):
    pdb = Pdb.objects.get(code=code)
    chains = list(pdb.chains.values_list('chain_id',flat=True))
    return render(request, 'symmetry/d3_projections.html',{'code':code,'pdb':pdb,'chains':chains})

def d3_json(request,code):
    pdb = Pdb.objects.get(code=code)
    return JsonResponse(pdb.unit_cell.projections)

def space_groups(request,num):
    "List all pdbs in this space group"
    pdbs = Pdb.objects.filter(unit_cell__num = num)
    return render(request, 'symmetry/space_groups.html',{'pdbs':pdbs})
