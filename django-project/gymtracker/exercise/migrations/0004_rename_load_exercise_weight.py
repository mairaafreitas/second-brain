# Generated by Django 4.1.4 on 2022-12-26 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("exercise", "0003_musculargroup"),
    ]

    operations = [
        migrations.RenameField(
            model_name="exercise",
            old_name="load",
            new_name="weight",
        ),
    ]
