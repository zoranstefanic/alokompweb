from django.shortcuts import render
from django.views.generic import ListView, DetailView
from pdbase.models import *
from .models import *

def alignments(request,code,chainid):
    fixed = Alignment.objects.filter(chain_fixed__pdb__code=code,chain_fixed__chain_id=chainid).order_by('-Qscore')
    moving = Alignment.objects.filter(chain_moving__pdb__code=code,chain_moving__chain_id=chainid).order_by('-Qscore')
    return render(request, 'alignments/alignments.html', {'fixed':fixed,'moving':moving})
