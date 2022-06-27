"""projeto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from portal_noticias import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('noticia/cadastrar', views.cadastro_noticia, name="cadastro_noticia"),
    path('noticia/cadastrar/cadastrar_genero', views.cadastro_genero, name="cadastro_genero"),
    path('noticia/cadastrar/cadastrar_genero/remover/<int:pk>', views.remover_genero, name="remover_genero"),
    path('noticia/<int:pk>', views.consultar_noticia, name="consulta_noticia"),

    path('administrar_noticias', views.administrar_noticias, name="administrar_noticias"),
    path('administrar_noticias/editar/<int:pk>', views.editar_noticia, name="editar_noticia"),
    path('administrar_noticias/remover/<int:pk>', views.remover_noticia, name="remover_noticia")
]
