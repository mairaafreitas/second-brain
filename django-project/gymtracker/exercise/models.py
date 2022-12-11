import uuid

from django.db import models


class Exercise(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Id")
    name = models.CharField(verbose_name="Nome", max_length=50, null=False, blank=False, unique=True)
    load = models.IntegerField(verbose_name="Carga", null=False, blank=False)
    repetitions = models.IntegerField(verbose_name="Número de repetições", null=False, blank=False)
    series = models.IntegerField(verbose_name="Número de séries", null=False, blank=False)


class MuscularGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Id")
    name = models.CharField(verbose_name="Nome", max_length=50, null=False, blank=False, unique=True)
    exercise = models.ForeignKey(
        Exercise, on_delete=models.SET_NULL, verbose_name="Exercício", null=True
    )
