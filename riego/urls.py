"""agua URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from riego import*
from .import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('listaAgua', views.listaAgua, name='listaAgua'),
    path('crearAgua/', views.crearAgua, name='crearAgua'),
    path('eliminarAgua/<int:id>', views.eliminarAgua, name='eliminarAgua'),
    path('edicionAgua/<int:id>', views.edicionAgua, name='edicionAgua'),
    path('editarAgua/', views.editarAgua, name='editarAgua'),
    path('listaSar', views.listaSar, name='listaSar'),
    path('crearSar/', views.crearSar, name='crearSar'),
    path('edicionSar/<int:id>', views.edicionSar, name='edicionSar'),
    path('editarSar/', views.editarSar, name='editarSar'),
    path('eliminarSar/<int:id>', views.eliminarSar, name='eliminarSar'),
    path('displaySar', views.displaySar, name='displaySar'),
    path('crearAlcalinidad/', views.crearAlcalinidad, name='crearAlcalinidad'),
    path('listaAlcalinidad/', views.listaAlcalinidad, name='listaAlcalinidad'),
    path('eliminarAlcalinidad/<int:id>', views.eliminarAlcalinidad, name='eliminarAlcalinidad'),
    path('edicionAlcalinidad/<int:id>', views.edicionAlcalinidad, name='edicionAlcalinidad'),
    path('editarAlcalinidad/', views.editarAlcalinidad, name='editarAlcalinidad'),
    path('displayAlcalinidad', views.displayAlcalinidad, name='displayAlcalinidad'),
    path('crearDureza/', views.crearDureza, name='crearDureza'),
    path('listaDureza/', views.listaDureza, name='listaDureza'),
    path('eliminarDureza/<int:id>/', views.eliminarDureza, name='eliminarDureza'),
    path('edicionDureza/<int:id>/', views.edicionDureza, name='edicionDureza'),
    path('editarDureza/', views.editarDureza, name='editarDureza'),
    path('displayDureza', views.displayDureza, name='displayDureza'),
]
