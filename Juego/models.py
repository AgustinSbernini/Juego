from django.db import models

class Usuario(models.Model):
    nick = models.CharField(max_length=50, null=False, blank=False)
    preguntasAcertadas = models.IntegerField(default=0)
    tiempo = models.CharField(max_length= 10, default = "00m 00s")
    puntaje = models.IntegerField(default=0)
    posicion = models.IntegerField(default=0)
    generoElegido = models.CharField(max_length= 10, default = "Historia")

    def __str__(self) -> str:
        return self.nick
