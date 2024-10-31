from django.contrib import admin

from .models import VentasAContribuyente, VentasAConsumidorFinal, Compras

admin.site.register(VentasAConsumidorFinal)
admin.site.register(VentasAContribuyente)
admin.site.register(Compras)
