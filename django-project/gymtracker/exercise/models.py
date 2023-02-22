from core.common_models import StandardModelMixin
from django.core.validators import RegexValidator
from django.db import models


class Exercise(StandardModelMixin):
    name = models.CharField(
        verbose_name="Nome", max_length=50, null=False, blank=False, unique=True
    )
    weight = models.IntegerField(
        verbose_name="Carga",
        null=False,
        blank=False,
        validators=[RegexValidator(r"^[0-9]", "Weight should have only numbers")],
    )
    repetitions = models.IntegerField(
        verbose_name="Número de repetições",
        null=False,
        blank=False,
        validators=[RegexValidator(r"^[0-9]", "Repetitions should have only numbers")],
    )
    series = models.IntegerField(
        verbose_name="Número de séries",
        null=False,
        blank=False,
        validators=[RegexValidator(r"^[0-9]", "Series should have only numbers")],
    )

    def __str__(self):
        return self.name

    class Meta:
        pass


class MuscularGroup(StandardModelMixin):
    name = models.CharField(
        verbose_name="Nome", max_length=50, null=False, blank=False, unique=True
    )
    exercise = models.ForeignKey(
        Exercise, on_delete=models.SET_NULL, verbose_name="Exercício", null=True
    )

    def __str__(self):
        return self.name
