from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from .models import *
from pdbase.models import Pdb

def structure_symmetry(request,code):
    pdb = Pdb.objects.get(code=code)
    return render(request, 'symmetry/structure_symmetry.html', 
                    {
                    'code':code,
                    'pdb':pdb,
                    }
                )

def symmetry_gallery(request):
    pdbs = Pdb.objects.all()
    return render(request, 'symmetry/symmetry_gallery.html',{'pdbs':pdbs} )

def d3_projections(request,code):
    pdb = Pdb.objects.get(code=code)
    return render(request, 'symmetry/d3_projections.html',{'code':code} )

def d3_json(request,code):
    pdb = Pdb.objects.get(code=code)
    return JsonResponse(pdb.unit_cell.projections)

