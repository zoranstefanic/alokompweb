from django.shortcuts import render
from django.shortcuts import redirect
from pdbase.models import Pdb

def search(request):
    if request.GET:
        q = request.GET.get('q')
        inCode = Pdb.objects.filter(code__icontains=q)
        inTitle = Pdb.objects.filter(title__icontains=q)
        inData = Pdb.objects.filter(data__sequence__icontains=q)
        results = inCode or inTitle or inData
        return render(request, 'search/search.html',
                      {
                       'query':q,
                       'results':results,
                       'inCode':inCode, 
                       'inTitle':inTitle, 
                       'inData':inData, 
                       })
    else:
        return render(request, 'search/search.html')
