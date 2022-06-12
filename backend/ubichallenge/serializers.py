from .models import AverageSpeed, Segment, Location
from rest_framework import serializers
from django.contrib.gis.geos import Point


class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = '__all__'


class SegmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Segment
    fields = '__all__'


class SpeedSerializer(serializers.ModelSerializer):
  class Meta:
    model = AverageSpeed
    fields = '__all__'
