from django.contrib import admin
from pages.models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        # implementa una columna con previsualizacion de la imagen de cada objeto del modelo tomando la url del fichero de imagen del campo 'photo'  
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.photo.url))
    thumbnail.short_description ='photo'

    # listado de los elementos del modelo a visualizar en Django Manager
    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_date')

    #elementos con enlaces para modificar los registros del modelo
    list_display_links = ('id', 'thumbnail', 'first_name')

    #implementa un buscador y los campos soportados para la busqueda
    search_fields = ('first_name', 'last_name', 'designation')

    #implementa un filtro de busqueda por el campo 'designation'
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin)