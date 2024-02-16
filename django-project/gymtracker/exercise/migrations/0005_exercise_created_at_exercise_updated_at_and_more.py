# Generated by Django 4.1.4 on 2022-12-29 11:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exercise", "0004_rename_load_exercise_weight"),
    ]

    operations = [
        migrations.AddField(
            model_name="exercise",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Criado em",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="exercise",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Atualizado em"),
        ),
        migrations.AddField(
            model_name="musculargroup",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Criado em",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="musculargroup",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Atualizado em"),
        ),
    ]