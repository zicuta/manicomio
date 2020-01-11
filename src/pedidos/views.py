from django.http import HttpResponse
from django.shortcuts import render
from .models import Comanda

# Create your views here.
def index (request):
    return render(request,'pedidos/index.html')
def guardar_pedido (request):
    print(request.POST['orden'])
    comanda=Comanda(orden=request.POST['orden'])
    comanda.save()
    return HttpResponse ('en breve entregamos su pedido')

    