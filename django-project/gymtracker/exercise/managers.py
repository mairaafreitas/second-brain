from django.db import models
from exercise.models import Exercise
from exercise.models import MuscularGroup


class ExerciseManager(models.Manager):
    def create(self, name, load, repetition, series, muscular_name):
        exercise = Exercise(name=name, load=load, repetition=repetition, series=series)
        exercise.save()
        muscular_group = MuscularGroup(
            name=muscular_name,
            exercise=exercise
        )
        muscular_group.save()
        return exercise
