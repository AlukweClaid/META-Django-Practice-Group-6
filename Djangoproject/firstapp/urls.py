from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('create-shoes/', views.createShoes,name='create-shoes'),
    path('create-clothes/', views.createClothes,name='create-clothes'),
    
]

    