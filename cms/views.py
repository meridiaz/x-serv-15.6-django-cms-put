from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Contenido

@csrf_exempt
def get_content(request, llave):
    if request.method == "PUT":
        valor = request.body.decode('utf-8')
        
        c = Contenido(clave=llave, valor=valor)
        c.save()
    try:
        respuesta = Contenido.objects.get(clave=llave).valor
    except Contenido.DoesNotExist:
        respuesta = "No existe contenido para la clave: " +llave
    return HttpResponse(respuesta)
