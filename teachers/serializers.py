from rest_framework import serializers
from .models import Teachers
import re

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teachers
        fields = '__all__'

    def validate_name(self, value):
        # if not value.replace(" ", "").isalpha():
        if not re.match(r'^[A-Za-z ]+$', value):
            raise serializers.ValidationError(
                "Only letters are allowed."
            )
        return value