from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class MSAalignmentView(DetailView):
    model = MSAlignment
    context_object_name = 'msa'
    template_name = "msa/msa.html"
