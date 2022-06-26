from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from portal_noticias.forms import FormNoticia, FormGenero
from portal_noticias.models import Noticia


def home(request):
    noticias = Noticia.objects.order_by('data_alteracao')

    context = {'noticias': noticias}
    return render(request, 'home.html', context)


def cadastro_noticia(request):
    if request.method == 'POST':
        form = FormNoticia(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = FormNoticia()

    context = {'form': form}
    return render(request, 'cadastro_noticia.html', context)


def cadastro_genero(request):
    if request.method == 'POST':
        form = FormGenero(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/noticia/cadastrar')
    else:
        form = FormGenero()

    context = {'form': form}
    return render(request, 'cadastro_genero.html', context)


def consultar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)

    context = {'noticia': noticia}
    return render(request, 'consultar_noticia.html', context)


def administrar_noticias(request):
    noticias = Noticia.objects.order_by('data_alteracao')

    context = {'noticias': noticias}
    return render(request, 'lista_noticias.html', context)


def editar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    form = FormNoticia(request.POST or None, instance=noticia)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/administrar_noticias')

    context = {'form': form}
    return render(request, 'cadastro_noticia.html', context)


def remover_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        noticia.delete()
        return HttpResponseRedirect('/administrar_noticias')

    context = {'noticia': noticia}
    return render(request, 'remover_noticia.html', context)
