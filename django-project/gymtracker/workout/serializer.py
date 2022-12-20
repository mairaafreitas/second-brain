"""Demonstration using class ModelSerializer"""

from workout.models import Workout
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """
    Nested Serializer
    """
    class Meta:
        model = User
        fields = ["name", "birth_date"]

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
    user = UserSerializer()

    class Meta:
        model = Workout
        fields = ["name", "exercise", "goal", "is_active"]
        exclude = ["id"]
        read_only_fields = ["end_at"]
        depth = 1
        extra_kwargs = {"name": {"read_only": True}}  # will be ignored since the field is explicitly declared
