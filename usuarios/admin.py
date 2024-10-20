from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from contabilidad.admin import custom_admin_site

from .models import User, Grupo


@admin.register(User, site=custom_admin_site)
class CustomUserAdmin(UserAdmin):
    """
    Usuario personalizado para admin
    """

    fieldsets = (
        ("Auntenticación", {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "groups",
                    "user_permissions",
                    "empresas",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    readonly_fields = ["last_login", "date_joined"]


@admin.register(Grupo, site=custom_admin_site)
class GrupoAdmin(GroupAdmin):
    pass
