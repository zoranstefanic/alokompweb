from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

def workplan(request):
    periods = Period.objects.all()
    return render(request,'workplan/workplan.html', {'periods':periods})
    
def wp_user(request,username):
    periods = Period.objects.filter(users__username=username)
    return render(request,'workplan/workplan.html', {'periods':periods})
