from django.http import HttpResponse
from .models import Comment

# Create your views here.
def test(request):
    return HttpResponse('200, Funciona todo OK papu')

def create(request):
    # comments = Comment(name='Juanjo', score=5, comment='Este es un comentario')
    # comments.save()
    
    comment = Comment.objects.create(name='Alex')
    return HttpResponse('test')

def delete(request):
    comment = Comment.objects.get(id=1)
    comment.delete()
    return HttpResponse('La base de datos ha sido dropeada XD')