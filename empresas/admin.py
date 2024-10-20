from django.contrib import admin

from contabilidad.admin import custom_admin_site

from .models import Empresa, Sucursal, Comprobante


@admin.register(Empresa, site=custom_admin_site)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "nrc", "nit"]
    ordering = ["nombre"]
    search_fields = ["nombre", "nrc"]


@admin.register(Sucursal, site=custom_admin_site)
class SucursalAdmin(admin.ModelAdmin):
    autocomplete_fields = ["empresa"]
    list_display = ["empresa_nombre", "nombre"]
    search_fields = ["nombre", "codigo"]

    @admin.display(description="empresa")
    def empresa_nombre(self, obj):
        return obj.empresa.nombre

    def get_form(self, request, obj=None, **kwargs):
        """
        El campo empresa no debe tener la posibilidad de borrado en este ModelAdmin
        """
        form = super().get_form(request, obj=None, **kwargs)
        form.base_fields["empresa"].widget.can_add_related = False
        form.base_fields["empresa"].widget.can_delete_related = False
        form.base_fields["empresa"].widget.can_change_related = False
        return form


@admin.register(Comprobante, site=custom_admin_site)
class ComprobanteAdmin(admin.ModelAdmin):
    autocomplete_fields = ["empresa"]

    def get_form(self, request, obj=None, **kwargs):
        """
        El campo empresa no debe tener la posibilidad de borrado en este ModelAdmin
        """
        form = super().get_form(request, obj=None, **kwargs)
        form.base_fields["empresa"].widget.can_add_related = False
        form.base_fields["empresa"].widget.can_delete_related = False
        form.base_fields["empresa"].widget.can_change_related = False
        return form
