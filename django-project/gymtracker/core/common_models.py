import uuid

from django.db import models


class StandardModelMixin(models.Model):
    """
    Abstract class for models.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Id")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        abstract = True
