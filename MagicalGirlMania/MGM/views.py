from django.shortcuts import render
#Para los forms preciso que me traiga los modelos
from MGM.models import Sailor, Winx, Witch
from MGM.forms import SailorForm, WinxForm, WitchForm


#Que en mis vistas me muestre lo que está en mis html
def index(request):
    return render (request, "MGM/index.html")

def winx(request):
    return render (request, "MGM/winx.html")
    
def witch(request):
    return render (request, "MGM/witch.html")

def sailor(request):
    return render (request, "MGM/sailor.html")

def sailorForm(request):
    if request.method == 'POST':
        sailorFormulario = SailorForm(request.POST)
        print(sailorFormulario)
        if sailorFormulario.is_valid():
            informacion = sailorFormulario.cleaned_data
            informacion = Sailor(categoria = informacion['categoria'], nombre = informacion['nombre'], planeta = informacion['planeta'], objeto = informacion['objeto'])
            informacion.save()
            return render(request, 'MGM/index.html')
    else:
        sailorFormulario = SailorForm()
        return render(request, 'MGM/sailorForm.html', {'sailorFormulario':sailorFormulario})

def winxForm(request):
    if request.method == 'POST':
        winxFormulario = WinxForm(request.POST)
        print(winxFormulario)
        if winxFormulario.is_valid():
            informacion = winxFormulario.cleaned_data
            informacion = Winx(categoria = informacion['categoria'], nombre = informacion['nombre'], hada = informacion['hada'], transformacion = informacion['transformacion'])
            informacion.save()
            return render(request, 'MGM/index.html')
    else:
        winxFormulario = WinxForm()
        return render(request, 'MGM/winxForm.html', {'winxFormulario':winxFormulario})

def witchForm(request):
    if request.method == 'POST':
        witchFormulario = WitchForm(request.POST)
        print(witchFormulario)
        if witchFormulario.is_valid():
            informacion = witchFormulario.cleaned_data
            informacion = Witch(categoria = informacion['categoria'], nombre = informacion['nombre'], elemento = informacion['elemento'], signo = informacion['signo'])
            informacion.save()
            return render(request, 'MGM/index.html')
    else:
        witchFormulario = WitchForm()
        return render(request, 'MGM/witchForm.html', {'witchFormulario':witchFormulario})
    
    