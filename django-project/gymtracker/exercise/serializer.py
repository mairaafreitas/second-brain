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
