from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'blog/index.html')


def alimentos(request):
    return render(request, 'blog/alimentos.html')

def ads(request):
    return render(request, 'blog/ads.html')

def apicultura(request):
    return render(request, 'blog/apicultura.html')

def informatica(request):
    return render(request, 'blog/informatica.html')