from django.shortcuts import render
from .models import Usuario
from Base_de_Datos.models import PreguntasYRespuestas
from django.http import HttpResponse
import random
import time

def index(request): 
    return render(request, 'index.html',{})

i = 0
respuestasCorrectas = 0
respCorr = 0
tiempoInicial = 0
tiempoActual = time.time()

def juego(request):
    global i
    global respuestasCorrectas
    global respCorr
    global contadorTiempo
    global tiempoInicial
    if i == 0:
        tiempoInicial = time.time()
    i+=1

    nick = request.POST['nick']
    genero = request.POST['genero']
    respuestaElegida = request.POST['respuestaElegida']

    if respCorr == respuestaElegida:
        respuestasCorrectas+=1
    
    preguntasSinUsar = PreguntasYRespuestas.objects.filter(genero=genero).filter(usada = 0)
    pregunta = random.choice(preguntasSinUsar)
    preguntaUsada = PreguntasYRespuestas.objects.get(id = pregunta.id)
    preguntaUsada.usada = 1
    preguntaUsada.save()

    respuestas = [pregunta.respuestaCorrecta, pregunta.respuestaIncorrecta1, pregunta.respuestaIncorrecta2, pregunta.respuestaIncorrecta3]
    random.shuffle(respuestas)
    respuesta1 = respuestas[0]
    respuesta2 = respuestas[1]
    respuesta3 = respuestas[2]
    respuesta4 = respuestas[3]
    
    respCorr = pregunta.respuestaCorrecta

    if i != 5:
        return render(request, 'juego.html',{'nick':nick, 'genero':genero, 'pregunta':pregunta, 
            'respuesta1':respuesta1, 'respuesta2':respuesta2, 'respuesta3':respuesta3, 'respuesta4':respuesta4})


    resetPregunta = PreguntasYRespuestas.objects.filter(genero=genero).filter(usada = 1)
    for preg in resetPregunta:
        preg.usada = 0
        preg.save()
    i = 0
    tiempoFinal = time.time()
    tiempoTotal = round(tiempoFinal - tiempoInicial, 0)
    puntaje = int((respuestasCorrectas*1000) - tiempoTotal)
    min = int(tiempoTotal / 60)
    seg = int(tiempoTotal % 60)
    if min < 10:
        min = f'0{min}'
    if seg < 10:
        seg = f'0{seg}'

    tiempoTotal = f'{min}m {seg}s'
    preguntasAcertadas = respuestasCorrectas
    respuestasCorrectas = 0

    usuario = Usuario(nick=nick, preguntasAcertadas=preguntasAcertadas, tiempo=str(tiempoTotal), puntaje=puntaje)
    usuario.save()

    usuariosOrdenados = Usuario.objects.all().order_by('-puntaje')[:10]
    posiciones = 0
    return render(request,'puntuaciones.html',{'usuariosOrdenados':usuariosOrdenados, 'preguntasAcertadas':preguntasAcertadas, 
    'tiempoTotal':tiempoTotal, 'puntaje':puntaje, 'posiciones':posiciones})