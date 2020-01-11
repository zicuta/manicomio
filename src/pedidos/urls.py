from django.contrib import admin
from django.urls import path
from .views import index, guardar_pedido

urlpatterns = [
    path('', index ),
    path('guardar/', guardar_pedido ),
    
]
