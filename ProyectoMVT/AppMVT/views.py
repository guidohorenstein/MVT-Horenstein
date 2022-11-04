from django.shortcuts import render
from .models import Familia
# Create your views here.
def mostrar_familiar(request):
    familiar1 = Familia(parentesco="Hermano", nombre="Guido", apellido="Horenstein", edad=19, nacimiento=[2, 10, 2003])
    familiar2 = Familia(parentesco="Hermana", nombre="Vera", apellido="Horenstein", edad=21, nacimiento=[19, 1, 2001])
    familiar3 = Familia(parentesco="Tia", nombre="Julia", apellido="Horenstein", edad=16, nacimiento=[4,9,2006])
    familiar4 = Familia(parentesco="Primo", nombre="Benjamin", apellido="Horenstein", edad=22, nacimiento=[17, 7, 2002])
    familiar5 = Familia(parentesco="Madre", nombre="Mariela", apellido="Mantegari", edad=53, nacimiento=[29, 6, 1969])

    return render(request, "familiares.html", {"listafamilia": [familiar1, familiar2, familiar3, familiar4, familiar5]})

#
#
#
#
#