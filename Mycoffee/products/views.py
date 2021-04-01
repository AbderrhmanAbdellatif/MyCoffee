from django.http import request
from django.shortcuts import render


def products(request):
    return render(request,'Products\products.html')
def product(request):
    return render(request,'Products\product.html')
def search(request):
    return render(request,'Products\search.html')
# Create your views here.
