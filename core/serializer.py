from rest_framework import serializers
from .models import SensorData


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['id', 'rate','oxygen','temperature']
