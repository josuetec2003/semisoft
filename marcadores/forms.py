from django.forms import ModelForm
from .models import Marcador

class MarcadorForm(ModelForm):
	class Meta():
		model = Marcador
		exclude = ("fecha",)