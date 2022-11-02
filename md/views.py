from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class MDdirectoriesView(ListView):
    model = MDdirectory
    context_object_name = 'directories'
    template_name = "md/directories.html"

class MDtrajectoriesView(ListView):
    model = MDtrajectory
    context_object_name = 'trajectories'
    template_name = "md/trajectories.html"

class MDdirectoryView(DetailView):
    model = MDdirectory
    context_object_name = 'directory'
    template_name = "md/directory.html"

class MDtrajectoryView(DetailView):
    model = MDtrajectory
    context_object_name = 'trajectory'
    template_name = "md/trajectory.html"
