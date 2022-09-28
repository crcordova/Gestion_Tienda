from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, "gestion_tienda/Home.html")

def ventas(request):
    return render(request, "gestion_tienda/ventas.html")

def compras(request):
    return render(request, "gestion_tienda/compras.html")