from django import forms
from django.forms import ModelForm

from portal_noticias.models import Genero, Noticia


class FormGenero(ModelForm):
    class Meta:
        model = Genero
        fields = ['descricao']
        labels = {'descricao': 'Descrição'}
        widgets = {
            'descricao': forms.TextInput(attrs={'max-length': 50})
        }


class FormNoticia(ModelForm):
    class Meta:
        model = Noticia
        fields = ['genero', 'titulo', 'conteudo', 'url_imagem', 'nome_autor']
        labels = {
            'genero': 'Gênero',
            'titulo': 'Título',
            'conteudo': 'Conteúdo',
            'url_imagem': 'URL da imagem',
            'nome_autor': 'Nome do autor'
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título da notícia', 'max-length': 150}),
            'conteudo': forms.Textarea(attrs={'placeholder': 'Digite aqui o conteúdo na sua notícia'}),
            'url_imagem': forms.TextInput(attrs={'placeholder': 'https://sua_imagem.jpeg'}),
            'nome_autor': forms.TextInput(attrs={'max-length': 100})
        }
