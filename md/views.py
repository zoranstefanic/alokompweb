from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class MDdirectories(ListView):
    model = MDdirectory
    context_object_name = 'directories'
    template_name = "md/directories.html"

class MDdirectory(DetailView):
    model = MDdirectory
    context_object_name = 'directory'
    template_name = "md/directory.html"

class Trajectory(DetailView):
    model = MDtrajectory
    context_object_name = 'trajectory'
    template_name = "md/trajectory.html"
