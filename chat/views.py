from django.shortcuts import render, redirect
from .models import Canal, Mensaje
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def canal(request, canal):
    nombre_usuario = request.GET.get('nombre_usuario')
    canal_detalles = Canal.objects.get(nombre=canal)
    return render(request, 'canal.html', {
        'nombre_usuario': nombre_usuario,
        'canal': canal,
        'canal_detalles': canal_detalles
    })

def checkview(request):
    canal = request.POST['nombre_canal']
    nombre_usuario = request.POST['nombre_usuario']

    if Canal.objects.filter(nombre=canal).exists():
        return redirect('/' + canal + '/?nombre_usuario=' + nombre_usuario)
    else:
        nuevo_canal = Canal.objects.create(nombre=canal)
        nuevo_canal.save()
        return redirect('/' + canal + '/?nombre_usuario=' + nombre_usuario)

def enviar(request):
    mensaje = request.POST['mensaje']
    nombre_usuario = request.POST['nombre_usuario']
    id_canal = request.POST['id_canal']

    nuevo_mensaje = Mensaje.objects.create(contenido=mensaje, usuario=nombre_usuario, canal=id_canal)
    nuevo_mensaje.save()
    return HttpResponse('Mensaje enviado correctamente')

def getMensajes(request, canal):
    canal_detalles = Canal.objects.get(nombre=canal)
    mensajes = Mensaje.objects.filter(canal=canal_detalles.id)
    return JsonResponse({"mensajes":list(mensajes.values())})