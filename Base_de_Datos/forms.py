from django import forms
genero_opciones = (
( "Historia" , "Historia" ),
( "Geografia" , "Geografia" ),
)
class crearPreguntaNueva(forms.Form):
    pregunta = forms.CharField(max_length=255, required = True)
    respuestaCorrecta = forms.CharField(max_length=255, required = True)
    respuestaIncorrecta1 = forms.CharField(max_length=255, required = True)
    respuestaIncorrecta2 = forms.CharField(max_length=255, required = True)
    respuestaIncorrecta3 = forms.CharField(max_length=255, required = True)
    genero = forms.ChoiceField(choices=genero_opciones)
