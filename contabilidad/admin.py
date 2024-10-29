from django.contrib import admin
from django.contrib.admin.views.autocomplete import AutocompleteJsonView
from .models import VentasAContribuyente, VentasAConsumidorFinal, Compras


class CustomAdminSite(admin.AdminSite):

    def autocomplete_view(self, request):
        if (
            request.GET["field_name"] == "proveedor"
            or request.GET["field_name"] == "cliente"
        ):
            return CustomAutocompleteJsonViewContacto.as_view(admin_site=self)(request)
        return super().autocomplete_view(request)


class CustomAutocompleteJsonViewContacto(AutocompleteJsonView):
    """
    Vista personalizad por si el modelo es un contacto
    """

    def serialize_result(self, obj, to_field_name):
        """
        Agrego el dato de la clasificación del contacto.
        """
        return {
            "id": str(getattr(obj, to_field_name)),
            "text": str(obj),
            "clasificacion": obj.clasificacion,
        }


custom_admin_site = CustomAdminSite(name="custom_admin_site")
custom_admin_site.site_header = "Econta"
custom_admin_site.site_title = "Econta"


@admin.register(VentasAConsumidorFinal, site=custom_admin_site)
class VentasAConsumidorFinalAdmin(admin.ModelAdmin):
    autocomplete_fields = ["empresa", "sucursal", "cliente"]
    fields = [
        ("empresa", "sucursal"),
        (
            "tipo_de_comprobante",
            "serie_de_documento",
            "numero_de_resolucion",
            "numero_de_documento",
        ),
        ("cliente", "fecha", "tipo_de_venta"),
        (
            "ventas_gravadas",
            "ventas_no_sujetas",
            "ventas_exentas",
            "sub_total",
            "retencion_de_iva",
        ),
        ("total",),
    ]
    list_display = ["__str__", "fecha", "sucursal"]
    list_filter = ["empresa"]
    save_as = True

    class Media:
        css = {"all": ("admin/css/custom_admin.css",)}

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

    def get_queryset(self, request):
        print(request.path)
        if request.path.split("/")[-2] == self.model._meta.label_lower.split(".")[-1]:
            if request.GET.get("empresa__id__exact"):
                return super().get_queryset(request)
            else:
                return self.model.objects.none()
        return super().get_queryset(request)


@admin.register(VentasAContribuyente, site=custom_admin_site)
class VentasAContribuyente(admin.ModelAdmin):
    autocomplete_fields = ["empresa", "sucursal", "cliente"]
    fields = [
        (
            "empresa",
            "sucursal",
            "serie_de_documento",
            "numero_de_resolucion",
            "numero_de_documento",
        ),
        ("cliente", "fecha"),
        ("ventas_gravadas", "iva", "sub_total"),
        ("ventas_no_sujetas", "ventas_exentas", "retencion_de_iva"),
        "total",
    ]
    list_filter = ["empresa"]
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

    def get_queryset(self, request):
        print(request.path)
        if request.path.split("/")[-2] == self.model._meta.label_lower.split(".")[-1]:
            if request.GET.get("empresa__id__exact"):
                return super().get_queryset(request)
            else:
                return self.model.objects.none()
        return super().get_queryset(request)

    class Media:
        css = {"all": ("admin/css/custom_admin.css",)}


@admin.register(Compras, site=custom_admin_site)
class ComprasAdmin(admin.ModelAdmin):
    autocomplete_fields = ["empresa", "proveedor"]
    fields = [
        ("empresa", "proveedor"),
        (
            "fecha",
            "tipo_de_compra",
            "tipo_de_comprobante",
            "numero_de_serie",
            "numero_de_comprobante",
        ),
        ("compra_neta", "iva", "sub_total", "percepcion_iva"),
        ("compra_excenta", "compra_excluida"),
        ("total", "tipo_de_gasto"),
    ]
    list_display = ["__str__", "empresa", "proveedor", "fecha"]
    list_filter = ["empresa"]
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

    def get_queryset(self, request):
        print(request.path)
        if request.path.split("/")[-2] == self.model._meta.label_lower.split(".")[-1]:
            if request.GET.get("empresa__id__exact"):
                return super().get_queryset(request)
            else:
                return self.model.objects.none()
        return super().get_queryset(request)

    class Media:
        css = {"all": ("admin/css/custom_admin.css",)}
