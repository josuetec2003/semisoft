from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Marcador
from .forms import MarcadorForm

def index(request):
	#return HttpResponse("Hola mundo")

	# Extraer los datos de la BD (Select)
	marcadores = Marcador.objects.all().order_by("-fecha")

	return render(request, "index.html", {"marcadores": marcadores})

def agregar_marcador(request):
	form = MarcadorForm()
	return render(request, "agregar_marcador.html", {"form": form})

def guardar_marcador(request):
	if request.method == 'POST':
		form = MarcadorForm(data = request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")
		else:
			return render(request, "agregar_marcador.html", {"form": form})

	else:
		return HttpResponse("No tienes acceso a esta URL")













