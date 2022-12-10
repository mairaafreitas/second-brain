import uuid

from django.db import models
from exercise.models import Exercise


class Workout(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Id")
    name = models.CharField(verbose_name="Nome", max_length=14, null=False, blank=False, unique=True)
    exercise = models.ForeignKey(
        Exercise, verbose_name="Comprovante", on_delete=models.SET_NULL, null=True
    )
