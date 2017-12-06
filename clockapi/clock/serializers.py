from rest_framework import serializers
from .models import Clock

class ClockSerializer (serializers.ModelSerializer):
    class Meta:
        model = Clock
        fields = '__all__'