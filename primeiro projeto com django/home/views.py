from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse('../teste.html do app')

def home(request):
    return render(request,'home/index.html') # devolvendo a pagina como html



