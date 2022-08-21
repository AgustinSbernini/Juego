from django.shortcuts import render
from django.http import HttpResponse
from .models import PreguntasYRespuestas
from .forms import crearPreguntaNueva

def create(request):
    crear_form = crearPreguntaNueva()
    return render(request, 'forms/create.html',{'crear_form':crear_form})

def success(request):
    pregunta = request.GET['pregunta']
    respuestaCorrecta = request.GET['respuestaCorrecta']
    respuestaIncorrecta1 = request.GET['respuestaIncorrecta1']
    respuestaIncorrecta2 = request.GET['respuestaIncorrecta2']
    respuestaIncorrecta3 = request.GET['respuestaIncorrecta3']
    genero = request.GET['genero']

    modeloPregunta = PreguntasYRespuestas(
        pregunta = pregunta, respuestaCorrecta = respuestaCorrecta, respuestaIncorrecta1 = respuestaIncorrecta1, 
        respuestaIncorrecta2 = respuestaIncorrecta2, respuestaIncorrecta3 = respuestaIncorrecta3, genero = genero)
    modeloPregunta.save()
    
    return HttpResponse(f'{pregunta}/{respuestaCorrecta}/{respuestaIncorrecta1}/{respuestaIncorrecta2}/{respuestaIncorrecta3}/{genero}')


def updel(request):
    preguntasHistoria = PreguntasYRespuestas.objects.filter(genero = 'Historia')
    preguntasGeografia = PreguntasYRespuestas.objects.filter(genero = 'Geografia')

    return render(request,'forms/updel.html',{'preguntasHistoria':preguntasHistoria, 'preguntasGeografia':preguntasGeografia})

def delete(request):
    idRecibido = request.GET['delete']
    pregunta = PreguntasYRespuestas.objects.get(id = idRecibido)
    pregunta.delete()

    return HttpResponse(f"La pregunta con id: {idRecibido} fue borrada exitosamente.")
  

def update(request):
    idRecibido = request.GET['update']
    preguntaRecibida = PreguntasYRespuestas.objects.get(id = idRecibido)

    return render(request,'forms/update.html',{'preguntaRecibida':preguntaRecibida})

def updateSuccess(request):
    idRecibido = request.GET['id']
    pregunta = request.GET['pregunta']
    respuestaCorrecta = request.GET['respuestaCorrecta']
    respuestaIncorrecta1 = request.GET['respuestaIncorrecta1']
    respuestaIncorrecta2 = request.GET['respuestaIncorrecta2']
    respuestaIncorrecta3 = request.GET['respuestaIncorrecta3']
    genero = request.GET['genero']

    preguntaActualizada = PreguntasYRespuestas.objects.get(id = idRecibido)
    
    preguntaActualizada.pregunta = pregunta 
    preguntaActualizada.respuestaCorrecta = respuestaCorrecta
    preguntaActualizada.respuestaIncorrecta1 = respuestaIncorrecta1
    preguntaActualizada.respuestaIncorrecta2 = respuestaIncorrecta2
    preguntaActualizada.respuestaIncorrecta3 = respuestaIncorrecta3
    preguntaActualizada.genero = genero
    
    preguntaActualizada.save()

    return HttpResponse(f"La pregunta con id: {idRecibido} fue actualizada exitosamente.")