from io import BytesIO
from tempfile import NamedTemporaryFile
import zipfile
from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.urls import path

from contabilidad.admin import custom_admin_site
from contabilidad.forms import GenerarLibrosYReportesMensualesDeEmpresaForm
from contabilidad.reports import crear_reporte_de_compras

from .models import Empresa, Sucursal, Comprobante


@admin.register(Empresa, site=custom_admin_site)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "nrc", "nit"]
    ordering = ["nombre"]
    search_fields = ["nombre", "nrc"]

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                "<path:object_id>/solicitar_libros_y_reportes_mensuales_de_la_empresa/",
                self.admin_site.admin_view(
                    self.solicitar_libros_y_reportes_mensuales_de_la_empresa
                ),
                name="solicitar_libros_y_reportes_mensuales_de_la_empresa",
            )
        ]
        return my_urls + urls

    def solicitar_libros_y_reportes_mensuales_de_la_empresa(self, request, object_id):
        """
        Vista del ModelAdmin que toma un formulario para descargar
        los libros y reportes mensuales de la empresa
        """
        empresa = self.get_object(request, object_id)
        context = dict(
            # Incluimos las variables de contexto del sitio
            **self.admin_site.each_context(request),
            opts=self.opts,
            object=object,
        )
        if self.has_change_permission(request, obj=None):
            if request.method == "POST":
                form = GenerarLibrosYReportesMensualesDeEmpresaForm(request.POST)
                if form.is_valid():
                    byte_data = BytesIO()
                    zip_file = zipfile.ZipFile(file=byte_data, mode="w")
                    reporte_de_compras = crear_reporte_de_compras(
                        empresa=empresa,
                        año=form.cleaned_data["año"],
                        mes=form.cleaned_data["mes"],
                    )
                    reportes_descripcion_corta = f"{empresa.nombre}_libros_y_reportes_{form.cleaned_data['año']}_{form.cleaned_data['mes']}"
                    with NamedTemporaryFile() as tmp:
                        reporte_de_compras.output(tmp.name)
                        tmp.seek(0)
                        stream = tmp.read()
                        zip_file.writestr(
                            f"Compras-{reportes_descripcion_corta}.pdf", stream
                        )
                    zip_file.close()
                    response = HttpResponse(
                        byte_data.getvalue(), content_type="application/zip"
                    )
                    response["Content-Disposition"] = (
                        f"attachment; filename={reportes_descripcion_corta}.zip"
                    )
                    return response
                else:
                    context["adminform"] = admin.helpers.AdminForm(
                        form=form,
                        fieldsets=[
                            (
                                "Ingrese los datos para generar los reportes y libros",
                                {
                                    "fields": GenerarLibrosYReportesMensualesDeEmpresaForm.base_fields
                                },
                            )
                        ],
                        prepopulated_fields=self.get_prepopulated_fields(
                            request=request
                        ),
                    )
                    return TemplateResponse(
                        request,
                        template="admin/empresas/libros_reportes_form.html",
                        context=context,
                    )
            context["adminform"] = admin.helpers.AdminForm(
                form=GenerarLibrosYReportesMensualesDeEmpresaForm(),
                fieldsets=[
                    (
                        "Ingrese los datos para generar los reportes y libros",
                        {
                            "fields": GenerarLibrosYReportesMensualesDeEmpresaForm.base_fields
                        },
                    )
                ],
                prepopulated_fields=self.get_prepopulated_fields(request=request),
            )
            return TemplateResponse(
                request=request,
                template="admin/empresas/libros_reportes_form.html",
                context=context,
            )
        else:
            raise PermissionDenied


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
