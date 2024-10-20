from django.contrib import admin
from django.contrib.admin.views.autocomplete import AutocompleteJsonView

from .models import VentasAContribuyente, VentasAConsumidorFinal, Compras


class CustomAdminSite(admin.AdminSite):

    def autocomplete_view(self, request):
        if request.GET["field_name"] == "numero_sucursal":
            return CustomAutocompleteJsonView.as_view(admin_site=self)(request)
        return super().autocomplete_view(request)


class CustomAutocompleteJsonView(AutocompleteJsonView):
    def serialize_result(self, obj, to_field_name):
        """
        Convert the provided model object to a dictionary that is added to the
        results list.
        """
        return {
            "id": str(getattr(obj, to_field_name)),
            "text": str(obj),
            "No_sucursal": obj.codigo,
        }


custom_admin_site = CustomAdminSite(name="custom_admin_site")
custom_admin_site.site_header = "Econta"
custom_admin_site.site_title = "Econta"


@admin.register(VentasAConsumidorFinal, site=custom_admin_site)
class VentasAConsumidorFinalAdmin(admin.ModelAdmin):
    autocomplete_fields = ["empresa", "sucursal", "cliente"]
    change_form_template = "admin/change_form_block.html"
    fields = [
        ("empresa", "sucursal"),
        ("tipo_de_comprobante", "serie_de_documento", "numero_de_documento"),
        ("cliente", "fecha", "tipo_de_venta"),
        ("ventas_gravadas", "ventas_no_sujetas", "ventas_exentas", "sub_total", "retencion_de_iva"),
        ("total",)
    ]
    save_as = True

    class Media:
        css = {
            "all": ("admin/css/custom_admin.css",)
        }

    def get_form(self, request, obj=None, **kwargs):
        """
        El campo empresa no debe tener la posibilidad de borrado en este ModelAdmin
        """
        form = super().get_form(request, obj=None, **kwargs)
        form.base_fields["empresa"].widget.can_add_related = False
        form.base_fields["empresa"].widget.can_delete_related = False
        form.base_fields["empresa"].widget.can_change_related = False
        form.base_fields["sucursal"].widget.can_add_related = False
        form.base_fields["sucursal"].widget.can_delete_related = False
        form.base_fields["sucursal"].widget.can_change_related = False
        form.base_fields["cliente"].widget.can_add_related = False
        form.base_fields["cliente"].widget.can_delete_related = False
        form.base_fields["cliente"].widget.can_change_related = False
        return form


@admin.register(VentasAContribuyente, site=custom_admin_site)
class VentasAContribuyente(admin.ModelAdmin):
    autocomplete_fields = ["empresa", "sucursal", "cliente"]
    change_form_template = "admin/change_form_block.html"
    fields = [
        ("empresa", "sucursal"),
        ("tipo_de_comprobate", "serie_de_documento", "numero_de_documento"),
        ("cliente", "fecha"),
        (
            "ventas_gravadas",
            "ventas_no_sujetas",
            "ventas_exentas",
            "iva",
            "sub_total",
            "retencion_de_iva",
        ),
        "total",
    ]
    save_as = True

    def get_form(self, request, obj=None, **kwargs):
        """
        El campo empresa no debe tener la posibilidad de borrado en este ModelAdmin
        """
        form = super().get_form(request, obj=None, **kwargs)
        form.base_fields["empresa"].widget.can_add_related = False
        form.base_fields["empresa"].widget.can_delete_related = False
        form.base_fields["empresa"].widget.can_change_related = False
        form.base_fields["sucursal"].widget.can_add_related = False
        form.base_fields["sucursal"].widget.can_delete_related = False
        form.base_fields["sucursal"].widget.can_change_related = False
        form.base_fields["cliente"].widget.can_add_related = False
        form.base_fields["cliente"].widget.can_delete_related = False
        form.base_fields["cliente"].widget.can_change_related = False
        return form

    class Media:
        css = {"all": ("admin/css/custom_admin.css",)}


@admin.register(Compras, site=custom_admin_site)
class ComprasAdmin(admin.ModelAdmin):
    autocomplete_fields = ["empresa", "proveedor"]
    change_form_template = "admin/change_form_block.html"
    fields = [
        ("empresa", "proveedor"),
        ("fecha", "tipo_de_compra", "tipo_de_comprobante", "numero_de_serie"),
        ("compra_neta", "iva", "percepcion_iva", "sub_total"),
        ("compra_excenta", "compra_excluida"),
        ("total", "tipo_de_gasto")
        
    ]
    save_as = True

    def get_form(self, request, obj=None, **kwargs):
        """
        El campo empresa no debe tener la posibilidad de borrado en este ModelAdmin
        """
        form = super().get_form(request, obj=None, **kwargs)
        form.base_fields["empresa"].widget.can_add_related = False
        form.base_fields["empresa"].widget.can_delete_related = False
        form.base_fields["empresa"].widget.can_change_related = False
        form.base_fields["proveedor"].widget.can_add_related = False
        form.base_fields["proveedor"].widget.can_delete_related = False
        form.base_fields["proveedor"].widget.can_change_related = False
        return form
    
    class Media:
        css = {
            "all": ("admin/css/custom_admin.css",)
        }
