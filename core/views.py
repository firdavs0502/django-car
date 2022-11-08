from django.shortcuts import render

def ferrari(request):
    return render(request, 'ferari.html')

def chevrolet(request):
    return render(request, 'chevralet.html')

def lambo(request):
    return render(request, 'lambo.html')

def mers(request):
    return render(request, 'mers.html')

def rols(request):
    return render(request, 'rolsroyse.html')
