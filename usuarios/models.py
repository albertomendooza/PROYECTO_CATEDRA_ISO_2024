from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.translation import gettext_lazy as _

from empresas.models import Empresa

class User(AbstractUser):
    """
    Usuario de sistema
    """

    empresas = models.ManyToManyField(
        to=Empresa,
        blank=True,
    )
    class Meta:
        verbose_name = " Usuario"
        verbose_name_plural = " Usuarios"


class Grupo(Group):
    """
    Modelo Proxy de Group para nuestro Admin
    """

    class Meta:
        proxy = True
