from typing import Dict

from exercise.models import Exercise
from rest_framework import serializers


def send_email(message_from, message):
    pass


class ExerciseSerializer(serializers.Serializer):
    """

    """
    name = serializers.CharField(max_length=50, allow_null=False, allow_blank=False, )
    load = serializers.IntegerField(default=0)
    repetitions = serializers.IntegerField()
    series = serializers.IntegerField()

    def validate(self, data: Dict) -> Dict:
        """
        When a validation requires access to multiple fields, need to add this method `validate()`.
        """
        if not data["repetitions"] and not data["series"]:
            raise serializers.ValidationError("You must set repetitions and series")
        return data

    def create(self, validated_data: Dict) -> Exercise:
        return Exercise.objects.create(**validated_data)

    def update(self, instance: Exercise, validated_data: Dict) -> Exercise:
        """
        To update, need to implement this method `update()`.
        It's possible to save aditional data when saving the instance.
        Example:
             instance.save(date=request.date)
        """
        instance.name = validated_data.get("name", instance.name)
        instance.load = validated_data.get("load", instance.load)
        instance.repetitions = validated_data.get("repetitions", instance.repetitions)
        instance.series = validated_data.get("series", instance.series)
        instance.save(update_fields=[
            "name",
            "load",
            "repetitions",
            "series",
        ])
        return instance

def validate_exercise():
    """
    Function `is_valid()` perform validations for each field of the serializer.
    You always need to call `is_valid()` before attempting to access the validated data, or save an object instance.

    If validation process succeed, `is_valid` set a `validated_data` dictionary.
    Otherwise, serializer's property `errors` will contain information about errors.

    `raise_exception` is optional.
    """
    data = {"name": "supino", "load": 10, "repetitions": 12, "series": 4}
    serializer = ExerciseSerializer(data=data)

    serializer.is_valid(raise_exception=True)
    return serializer.validated_data
