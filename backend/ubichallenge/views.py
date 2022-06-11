#from django.shortcuts import render
from rest_framework import generics
from .models import Segment
from .serializers import SegmentSerializer


# CRUD for Segment with IDs
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