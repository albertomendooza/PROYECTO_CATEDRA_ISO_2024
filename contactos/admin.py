from django.contrib import admin

from contabilidad.admin import custom_admin_site

from .models import Contacto, ConsumidorFinal


@admin.register(Contacto, site=custom_admin_site)
class ContactoAdmin(admin.ModelAdmin):
    search_fields = ["nombre", "nrc"]


@admin.register(ConsumidorFinal, site=custom_admin_site)
class ConsumidorFinalAdmin(admin.ModelAdmin):
    search_fields = ["nombre", "numero_de_documento"]
