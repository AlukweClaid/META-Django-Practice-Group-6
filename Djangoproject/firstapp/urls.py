from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('create-shoes/', views.createShoes, name='create-shoes'),
    path('create-clothes/', views.createClothes, name='create-clothes'),
    path('hello/', views.ourfirstapp, name='hello'),

    # Shoes CRUD
    path('shoes/', views.fetchAllShoes, name='fetchAll'),
    path('shoes/<int:pk>/', views.shoes_detail, name='shoes-detail'),
    path('shoes/<int:pk>/edit/', views.updateShoes, name='update-shoes'),
    path('shoes/<int:pk>/delete/', views.deleteShoes, name='delete-shoes'),

    # Clothes CRUD (optional)
    path('clothes/', views.fetchAllClothes, name='fetchAllClothes'),
    path('clothes/<int:pk>/', views.clothes_detail, name='clothes-detail'),
    path('clothes/<int:pk>/edit/', views.updateClothes, name='update-clothes'),
    path('clothes/<int:pk>/delete/', views.deleteClothes, name='delete-clothes'),
]

    