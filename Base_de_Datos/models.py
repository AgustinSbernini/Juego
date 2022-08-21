from django.db import models

class PreguntasYRespuestas(models.Model):
    pregunta = models.CharField(max_length=255, null=False, blank=False)
    respuestaCorrecta = models.CharField(max_length=255, null=False, blank=False)
    respuestaIncorrecta1 = models.CharField(max_length=255, null=False, blank=False)
    respuestaIncorrecta2 = models.CharField(max_length=255, null=False, blank=False)
    respuestaIncorrecta3 = models.CharField(max_length=255, null=False, blank=False)
    genero = models.CharField(max_length=255, null=False, blank=False, default='Historia')
    usada = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.pregunta