# Generated by Django 4.1.4 on 2022-12-10 10:53

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("exercise", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Workout",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Id",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=14, unique=True, verbose_name="Nome"),
                ),
                (
                    "exercise",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="exercise.exercise",
                        verbose_name="Comprovante",
                    ),
                ),
            ],
        ),
    ]
