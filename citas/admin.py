from django.contrib import admin

# Register your models here.


from .models import Lugares, Critica_sitios, Sitios_visitados

admin.site.register(Lugares)
admin.site.register(Critica_sitios)
admin.site.register(Sitios_visitados)