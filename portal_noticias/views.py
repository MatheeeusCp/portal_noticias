from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from portal_noticias.forms import FormNoticia, FormGenero
from portal_noticias.models import Noticia, Genero


def home(request):
    noticias = Noticia.objects.order_by('data_criacao')
    generos = Genero.objects.order_by('id')

    if request.method == 'POST':
        filter = request.POST.get('filter')
        genero_filter = request.POST.get('genero_filter')
        genero = Genero.objects.filter(descricao__exact=genero_filter)
        if len(genero) > 0:
            noticias = Noticia.objects.filter(titulo__contains=filter, genero_id__exact=genero[0].id)
        else:
            noticias = Noticia.objects.filter(titulo__contains=filter)

    context = {'noticias': noticias, 'generos': generos}
    return render(request, 'home.html', context)


def cadastro_noticia(request):
    if request.method == 'POST':
        form = FormNoticia(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = FormNoticia()

    context = {'form': form, 'cadastro': True}
    return render(request, 'cadastro_noticia.html', context)


def cadastro_genero(request):
    generos = Genero.objects.order_by('id')

    if request.method == 'POST':
        form = FormGenero(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/noticia/cadastrar')
    else:
        form = FormGenero()

    context = {'form': form, 'generos': generos}
    return render(request, 'cadastro_genero.html', context)


def consultar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)

    context = {'noticia': noticia}
    return render(request, 'consultar_noticia.html', context)


def administrar_noticias(request):
    noticias = Noticia.objects.order_by('data_criacao')
    generos = Genero.objects.order_by('id')

    if request.method == 'POST':
        filter = request.POST.get('filter')
        genero_filter = request.POST.get('genero_filter')
        genero = Genero.objects.filter(descricao__exact=genero_filter)
        if len(genero) > 0:
            noticias = Noticia.objects.filter(titulo__contains=filter, genero_id__exact=genero[0].id)
        else:
            noticias = Noticia.objects.filter(titulo__contains=filter)

    context = {'noticias': noticias, 'generos': generos}
    return render(request, 'lista_noticias.html', context)


def editar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)

    form = FormNoticia(request.POST or None, instance=noticia)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/administrar_noticias')

    context = {'form': form, 'cadastro': False}
    return render(request, 'cadastro_noticia.html', context)


def remover_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        noticia.delete()
        return HttpResponseRedirect('/administrar_noticias')

    context = {'noticia': noticia}
    return render(request, 'remover_noticia.html', context)


def remover_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    noticia_encontrada = Noticia.objects.filter(genero_id__exact=pk)
    if len(noticia_encontrada) == 0:
        genero.delete()
    else:
        messages.add_message(request, messages.ERROR, 'Há uma notícia cadastrada com este gênero.')

    return HttpResponseRedirect('/noticia/cadastrar/cadastrar_genero')
