from .models import AverageSpeed, Segment
from rest_framework import serializers


class SegmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Segment
    fields = '__all__'


class SpeedSerializer(serializers.ModelSerializer):
  class Meta:
    model = AverageSpeed
    fields = '__all__'