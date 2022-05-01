from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),       # 'name' permite llamar la url sin agregar la ruta a la etiqueta 'href'
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
]
