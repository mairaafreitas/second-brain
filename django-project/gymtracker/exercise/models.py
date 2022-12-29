import uuid

from django.db import models
from core.common_models import StandardModelMixin


class Exercise(StandardModelMixin):
    name = models.CharField(verbose_name="Nome", max_length=50, null=False, blank=False, unique=True)
    weight = models.IntegerField(verbose_name="Carga", null=False, blank=False)
    repetitions = models.IntegerField(verbose_name="Número de repetições", null=False, blank=False)
    series = models.IntegerField(verbose_name="Número de séries", null=False, blank=False)


class MuscularGroup(StandardModelMixin):
    name = models.CharField(verbose_name="Nome", max_length=50, null=False, blank=False, unique=True)
    exercise = models.ForeignKey(
        Exercise, on_delete=models.SET_NULL, verbose_name="Exercício", null=True
    )
