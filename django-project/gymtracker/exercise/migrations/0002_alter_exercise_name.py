# Generated by Django 4.1.4 on 2022-12-10 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exercise", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exercise",
            name="name",
            field=models.CharField(max_length=50, unique=True, verbose_name="Nome"),
        ),
    ]
