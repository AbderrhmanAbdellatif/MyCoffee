from django.urls import  path
from . import views #icinde buldugu dosyalari viwr al ve import et

urlpatterns = [
    path('index' ,views.index , name ='index'), #viwers icinde fonksiyonlarini def index() gibi index cagirmasi lazim 
    path('my1',views.my1,name ='my1'),
    path('my2',views.my2,name ='my2'),
    path('my3',views.my3,name ='my3'),
]