from typing import Dict

from exercise.models import Exercise
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


def send_email(message_from, message):
    pass


def greater_than_zero(value):
    """
    Method to use as validator.
    """
    if value < 0:
        raise serializers.ValidationError("Must be grater than 0.")


class ExerciseSerializer(serializers.Serializer):
    """
    Individual fields can include validators, declaring them in the field.

    UniqueValidator enforces the unique=True, `queryset` argument is required.
    """
    name = serializers.CharField(max_length=50, allow_null=False, allow_blank=False,
                                 validators=[UniqueValidator(queryset=Exercise.objects.all())])
    load = serializers.IntegerField(default=0)
    repetitions = serializers.IntegerField(required=True)
    series = serializers.IntegerField(required=True, validators=[greater_than_zero])


    def validate(self, data: Dict) -> Dict:
        """
        When a validation requires access to multiple fields, need to add this method `validate()`.
        :param data: dict of all fields values
        :return: returns validated all fields or ValidationError
        """
        if not data["repetitions"] and not data["series"]:
            raise serializers.ValidationError("You must set repetitions and series")
        return data

    def validate_repetitions(self, value: int) -> int:
        """
        It's possible to customize to validate one field, using `validate_<field_name>`.
        :param value: field that needs validation
        :return: returns validated field or ValidationError

        If field is required=False, this validation will not work if field is not included.
        """
        if value < 0:
            serializers.ValidationError("Repetitions must be greater than 0.")
        return value

    def create(self, validated_data: Dict) -> Exercise:
        return Exercise.objects.create(**validated_data)

    def update(self, instance: Exercise, validated_data: Dict) -> Exercise:
        """
        To update, need to implement this method `update()`.
        It's possible to save aditional data when saving the instance.
        Example:
             instance.save(date=request.date)

        Must be passed all required fields to serializer. To user partial updates, must pass as
        argument `partial=True`.
        Example:
            ExerciseSerializer(exercise, data={'load'=10}, partial=True)
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

    def _save(self):
        """
        In cases when methods create and update won't create or update an instance but instead do something else like
        send an email. You can override `.save()`
        """
        email = self.validated_data["email"]
        message = self.validated_data['message']
        send_email(message_from=email, message=message)


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
