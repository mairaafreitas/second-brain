from django.db import models
from exercise.models import Exercise, MuscularGroup


class ExerciseManager(models.Manager):
    def create(self, name, weight, repetition, series, muscular_name):
        exercise = Exercise(
            name=name, weight=weight, repetition=repetition, series=series
        )
        exercise.save()
        muscular_group = MuscularGroup(name=muscular_name, exercise=exercise)
        muscular_group.save()
        return exercise
