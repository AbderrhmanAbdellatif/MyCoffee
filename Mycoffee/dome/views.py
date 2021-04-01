from django.http import request
from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.

def index(request): # request paramtar olarak yazmamaiz lazim 
    return HttpResponse('<h1>Django easy </h1>')

def my1(request):
    return HttpResponse('<h1> my1 </h1>')

def my2(request):
    return HttpResponse('<h1> my2 </h1>')

def my3(request):
    return HttpResponse('<h1> my3 </h1>')
