from typing import Any
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

    def get_search_results(self, request, queryset, search_term):
        queryset, may_have_duplicates = super().get_search_results(
            request,
            queryset,
            search_term,
        )
        if request.path == "/admin/autocomplete/":
            empresa_id = request.GET.get("empresa_id")
            if empresa_id:
                queryset = queryset.filter(empresa__id=empresa_id)
                return queryset, may_have_duplicates
            else:
                return self.model.objects.none(), may_have_duplicates
        return super().get_search_results(request, queryset, search_term)


@admin.register(Comprobante, site=custom_admin_site)
class ComprobanteAdmin(admin.ModelAdmin):
    autocomplete_fields = ["empresa", "sucursal"]
    list_display = ["__str__", "empresa", "sucursal"]

    def save_model(self, request, obj, form, change):
        if obj.marcar_como_actual:
            actuales = Comprobante.objects.filter(
                empresa=obj.empresa,
                sucursal=obj.sucursal,
                tipo_de_comprobante=obj.tipo_de_comprobante,
                marcar_como_actual=True,
            )
            for comprobante in actuales:
                comprobante.marcar_como_actual = False
                comprobante.save()
        super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        """
        El campo empresa no debe tener la posibilidad de borrado en este ModelAdmin
        """
        form = super().get_form(request, obj=None, **kwargs)
        form.base_fields["empresa"].widget.can_add_related = False
        form.base_fields["empresa"].widget.can_delete_related = False
        form.base_fields["empresa"].widget.can_change_related = False
        return form
