from django.shortcuts import render
from django.views.generic import ListView, DetailView
from pdbase.models import *
from .models import *

class AlignmentsList(ListView):
    model = Alignment
    context_object_name = 'alignments'
    template_name = "alignments/alignments_list.html"
    paginate_by = "500"

def alignment1(request,code,chainid):
    fixed = Alignment.objects.filter(chain_fixed__pdb__code=code,chain_fixed__chain_id=chainid).order_by('-Qscore')
    moving = Alignment.objects.filter(chain_moving__pdb__code=code,chain_moving__chain_id=chainid).order_by('-Qscore')
    return render(request, 'alignments/alignments.html', {'fixed':fixed,'moving':moving})


def alignment(request,code1,chain1,code2,chain2):
    a = Alignment.objects.get(   chain_fixed__pdb__code=code1, 
                                    chain_fixed__chain_id = chain1,
                                    chain_moving__pdb__code=code2, 
                                    chain_moving__chain_id = chain2)
    positions = a.positions.all()
    return render(request, 'alignments/alignment.html', {'alignment':a,'positions':positions})

