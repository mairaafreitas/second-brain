from django.core.validators import MinValueValidator
from django.db import models


class Exercise(models.Model):
    name = models.CharField(verbose_name="Nome do exercício", max_length=80, null=False, blank=False)
    repetition = models.IntegerField(verbose_name="Repetições", null=False, blank=False,
                                     validators=MinValueValidator(0))
    series = models.IntegerField(verbose_name="Repetições", null=False, blank=False, validators=MinValueValidator(0))
    load = models.IntegerField(verbose_name="Repetições", null=False, blank=False, default=0)
