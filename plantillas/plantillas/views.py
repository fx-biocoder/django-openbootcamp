# from django.http import HttpResponse

# Renderizacion del contenido de los templates
from django.shortcuts import render

def simple(request):
    # regresa request, plantilla, y un contexto (un diccionario)
    return render(request, 'simple.html', {})

def dinamico(request, name: str):
    # igual anterior pero sumando contexto
    categories = ['code', 'design', 'marketing']
    context = {
        'name': name,
        'categories': categories
    }
    return render(request, 'dinamico.html', context)