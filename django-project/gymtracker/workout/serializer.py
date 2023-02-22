"""Demonstration using class ModelSerializer"""
from typing import Dict

from exercise.models import Exercise
from rest_framework import serializers
from workout.models import Workout


class ExerciseSerializer(serializers.ModelSerializer):
    """
    Nested Serializer
    """

    class Meta:
        model = Exercise
        fields = ["name", "weight", "repetitions", "series"]


class ExercisesSerializer(serializers.RelatedField):
    """
    RelatedField to custom relational field that describes output representation.
    To do this, need to override 'RelatedField' and add to_representation(self, value) method.
    """

    def to_representation(self, value):
        """
        :param value: model instance, Exercises
        :return: your custom representation
        """
        load = int(value.weight) * int(value.repetitions) * int(value.series)
        return "Exercise: %s x %s x %s -> total load: %s)" % (
            value.series,
            value.repetitions,
            value.weight,
            load,
        )

    def to_internal_value(self, data):
        """
        If is needed a read-write relational field, need to implement this method.
        """


class WorkoutSerializer(serializers.ModelSerializer):
    """
    ModelSerializer automatically create a Serializer corresponding to the Model fields. The main difference from
    Serializer is:
        - It will automatically generate a set of fields for you, based on the model.
        - It will automatically generate validators for the serializer, such as unique_together validators.
        - It includes simple default implementations of .create() and .update().

    `depth` option is used to set the depth of relationships before revert to a flat representation. If you want to
    customize, you need to define the field.

    Instead of explicity declare the field to specify additional keywords, you can use the `extra_kwargs` option.

    To add extra fields or override the default fields, declare it as you would at Serializer class.
    PS: Extra fields can correspond to any property or callable on the model.
    Example:
        full_name = serializers.CharField(source='get_full_name', read_only=True)
    """

    name = serializers.CharField(read_only=True)
    exercise = ExerciseSerializer(many=True)

    class Meta:
        model = Workout
        fields = ["name", "exercise", "goal", "is_active"]
        exclude = ["id"]
        read_only_fields = ["end_at"]
        depth = 1
        extra_kwargs = {
            "name": {"read_only": True}
        }  # will be ignored since the field is explicitly declared

    def create(self, validated_data: Dict) -> Workout:
        """
        By default nested serializers are read-only. You need to explicitly specify how the child relationships should
        be saved.
        """
        exercises_data = validated_data.pop("exercise")
        workout = Workout.objects.create(**validated_data)
        for exercise_data in exercises_data:
            Exercise.objects.create(workout=workout, **exercise_data)
        return workout

    def to_representation(self, instance):
        """
        Takes the object instance that requires serialization, and should return a primitive representation.
        Overriding this method allows us to change the serialization output
        """
        representation = super().to_representation(instance)
        representation["load"] = (
            int(instance.weight) * int(instance.repetitions) * int(instance.series)
        )

    def to_internal_value(self, data):
        """
        Used to do some pre-processing before validation. Could be used to extract some information.
        """
        exercise_data = data["exercise"]
        return super().to_internal_value(exercise_data)
