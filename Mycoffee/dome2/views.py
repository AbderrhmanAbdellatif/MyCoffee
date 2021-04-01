from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1>index form dome2</h1>')
def my1(request):
    return HttpResponse('<h1>my1 form dome2</h1>')
    