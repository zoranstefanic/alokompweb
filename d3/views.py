from django.shortcuts import render

def d3(request):
    return render(request, 'd3/index.html')
