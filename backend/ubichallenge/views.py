#from django.shortcuts import render
from rest_framework import generics
from .models import AverageSpeed, Segment
from .serializers import SegmentSerializer, SpeedSerializer
from rest_framework.response import Response
from rest_framework import status


# ---------------------------------------------------- CRUD for Segment with IDs
class SegmentCreateApi(generics.CreateAPIView):
  queryset = Segment.objects.all()
  serializer_class = SegmentSerializer


class SegmentListApi(generics.ListAPIView):
  queryset = Segment.objects.all()
  serializer_class = SegmentSerializer


class SegmentUpdateApi(generics.RetrieveUpdateAPIView):
  queryset = Segment.objects.all()
  serializer_class = SegmentSerializer


class SegmentDeleteApi(generics.DestroyAPIView):
  queryset = Segment.objects.all()
  serializer_class = SegmentSerializer


# ---------------------------------------------------- Crud for AverageSpeed with IDs
class SpeedCreateApi(generics.CreateAPIView):
  queryset = AverageSpeed.objects.all()
  serializer_class = SpeedSerializer


class SpeedListApi(generics.ListAPIView):
  queryset = AverageSpeed.objects.all()
  serializer_class = SpeedSerializer


class SpeedUpdateApi(generics.RetrieveUpdateAPIView):
  queryset = AverageSpeed.objects.all()
  serializer_class = SpeedSerializer


class SpeedDeleteApi(generics.DestroyAPIView):
  queryset = AverageSpeed.objects.all()
  serializer_class = SpeedSerializer
