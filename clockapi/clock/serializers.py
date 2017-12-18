from rest_framework import serializers
from .models import Clock

class ClockSerializer (serializers.ModelSerializer):
    class Meta:
        model = Clock
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_on': {'read_only': True},
            'updated_on': {'read_only': True},
            'user': {'read_only': True},
            'is_deleted': {'read_only': True}
        }