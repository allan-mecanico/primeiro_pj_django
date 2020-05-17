from django.shortcuts import render, redirect

from .form import TransacaoForm
from .models import Transacao
import _datetime


def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']
    data['now'] = _datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'contas/home.html', data)


def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    return render(request, 'contas/form.html', data)

def update(request, pk):
    data={}
    transacao = Transacao.objects.filter(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)


    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    return render(request, 'contas/form.html', data)
