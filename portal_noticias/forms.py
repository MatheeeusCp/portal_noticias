from django.forms import ModelForm

from portal_noticias.models import Noticia, Genero


class FormGenero(ModelForm):
    class Meta:
        model = Genero
        fields = ['descricao']


class FormNoticia(ModelForm):
    class Meta:
        model = Noticia
        fields = ['genero', 'titulo', 'conteudo', 'url_imagem', 'nome_autor']
