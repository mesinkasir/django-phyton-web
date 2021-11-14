from django.urls import path
from . import views

urlpatterns = [

path('index',views.index,name="index"),
path('pembuatanandroid',views.pembuatanandroid,name="pembuatanandroid"),
path('pembuatanwebsite',views.pembuatanwebsite,name="pembuatanwebsite"), 
path('pembuatanaplikasi',views.pembuatanaplikasi,name="pembuatanaplikasi"), 
]