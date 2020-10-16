from django.http import HttpResponse

#  Primera vista en Django

def saludo(request):
    # Respuesta
    return HttpResponse("Hola Mundo en primera página con Django :)")
