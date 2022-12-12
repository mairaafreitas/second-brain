import uuid

from django.db import models
from exercise.models import Exercise
from model_utils import Choices


class Workout(models.Model):
    # 3-tuples (db_value, python_identifier, "human_readable_string")
    GOAL_CHOICES = Choices(
        ("loseWeight", "LOSE_WEIGHT", "Emagrecimento"),
        ("resistance", "RESISTANCE", "Resistência"),
        ("hypertrophy", "HYPERTROPHY", "Hipertrofia"),
        ("strength", "STRENGTH", "Força")
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Id")
    name = models.CharField(verbose_name="Nome", max_length=14, null=False, blank=False, unique=True)
    exercise = models.ForeignKey(
        Exercise, verbose_name="Exercício", on_delete=models.SET_NULL, null=True
    )
    goal = models.CharField(
        verbose_name="Objetivo", null=False, blank=False, choices=GOAL_CHOICES, max_length=200
    )
    is_active = models.BooleanField(
        default=True, null=False, verbose_name="Treino ativo"
    )
    end_at = models.DateTimeField(verbose_name="Data da finalização do treino", null=True, blank=True)
