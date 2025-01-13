from rest_framework import serializers
from .models import Char

class CharSerializer(serializers.ModelSerializer):
    class Meta:
        model = Char
        fields = '__all__'