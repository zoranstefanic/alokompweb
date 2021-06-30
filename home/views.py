from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

def news(request):
    return render(request, 'news.html')

def gannt(request):
    return render(request, 'gannt.html')

def equipment(request):
    return render(request, 'equipment.html')

def results_xc(request):
    return render(request, 'results_xc.html')

def results_md(request):
    return render(request, 'results_md.html')

def results_ml(request):
    return render(request, 'template.html')
