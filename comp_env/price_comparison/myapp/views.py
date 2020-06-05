from django.shortcuts import render
from .models import amfp
from .sel_code import compare
# Create your views here.

def enterprod(request):
    a = amfp.objects.all()
    a.delete()
    return render(request, 'index.html')

def createtable(request):
    product=request.POST['product']
    compare(product)
    f = amfp.objects.all()
    return render(request, 'show.html', {'f': f})

