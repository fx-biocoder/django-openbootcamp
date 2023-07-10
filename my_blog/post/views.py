from django.shortcuts import render
from django.http import HttpResponse
from .models import Author
# Create your views here.

def queries(request):
    #   Obtener todos los autores y entradas
    authors = Author.objects.all()

    # Obtener datos filtrados por condición
    filtered = Author.objects.filter(email='gwhite@example.net')

    # Obtener un único dato filtrado
    author = Author.objects.get(id=1)

    # Obtener los 5 primeros elementos
    limits = Author.objects.all()[:5]

    # Obtener los 5 ultimos elementos
    last_five = Author.objects.all()[-5:]

    # Obtener 5 elementos saltando los cinco primeros
    skips = Author.objects.all()[5:10]

    # Obtener todos los elementos ordenados por email
    ordered = Author.objects.all().order_by('email')

    # Obtener todos los elementos cuyo id sea igual o menor a 10
    # lte = lower than or equal
    # gte = greater than or equal
    # lt = less than
    # gt = greater than
    # contains = contiene
    # startswith = empieza con
    # endswith = termina con
    # iexact = igual exacto
    # icontains = contiene exacto
    # istartswith = empieza con exacto
    # iendswith = termina con exacto
    
    less_than_ten = Author.objects.all().filter(id__lte=10)

    context = {
        'authors': authors,
        'filtered': filtered,
        'author': author,
        'limits': limits,
        'last_five': last_five,
        'skips': skips,
        'orders': ordered,
        'less_than_ten': less_than_ten
    }

    return render(request, 'post/queries.html', context)

# ----------------------------------------------------------------

# Actualizar datos de la tabla de la base de datos

"""
def update(request):
    if request.method == 'POST':
        author = Author.objects.get(id=1)
        author.name = request.POST['name']
        author.email = request.POST['email']
"""