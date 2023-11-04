from django import forms

#Campos clase Sailor Moon
class SailorForm(forms.Form):
    categoria = forms.CharField(max_length=6)
    nombre = forms.CharField(max_length=10)
    planeta = forms.CharField(max_length=50)
    objeto = forms.CharField(max_length=20)

#Campos form Winx
class WinxForm(forms.Form):
    categoria = forms.CharField(max_length=6)
    nombre = forms.CharField(max_length=10)
    hada = forms.CharField(max_length=50)
    transformacion = forms.CharField(max_length=20)

#Campos Form Witch
class WitchForm(forms.Form):
    categoria = forms.CharField(max_length=6)
    nombre = forms.CharField(max_length=10)
    elemento = forms.CharField(max_length=50)
    signo = forms.CharField(max_length=20)