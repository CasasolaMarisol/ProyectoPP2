from .models import caja
from django.forms import ModelForm

class apertura(ModelForm):
    class Meta:
        model=caja
        fields = ['Apertura_de_Caja','Saldo_Inicial']

class cierre(ModelForm):
    class Meta:
        model = caja
        fields = ['Cierre_de_Caja', 'Saldo_Total']