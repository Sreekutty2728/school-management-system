from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    def validate_name(self, value):
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError(
                "Name should contain only letters."
            )
        return value

    class Meta:
        model = Student
        fields = '__all__'