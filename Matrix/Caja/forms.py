from .models import Caja
from django.forms import ModelForm

class apertura(ModelForm):
    class Meta:
        model=Caja
        fields = ['fecha_apertura','saldo_inicial']

class cierre(ModelForm):
    class Meta:
        model = Caja
        fields = ['fecha_cierre', 'saldo_final']