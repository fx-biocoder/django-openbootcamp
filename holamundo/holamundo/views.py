from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo!")

def despedida(request):
    return HttpResponse('Adiós mundo cruel!')

def adulto(request, edad: int):
    if edad >= 18:
        return HttpResponse('Es mayor de edad!!!1!')
    else:
        return HttpResponse('No es adulto >:(')