from django.forms import ModelForm
from .models import Transacao
from _datetime import datetime


class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'valor', 'observacoes', 'categoria']

