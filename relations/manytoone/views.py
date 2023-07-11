from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article

# Create your views here.
def create(request):
    rep = Reporter(first_name='Juan', last_name='Perez', email='juan@gmail.com')
    rep.save()

    art1 = Article(reporter=rep, headline='Titulo 1')
    art2 = Article(reporter=rep, headline='Titulo 2')
    art3 = Article(reporter=rep, headline='Titulo 3')
    art1.save()
    art2.save()
    art3.save()
    

    return HttpResponse('Creado.')