#from django.shortcuts import render
from rest_framework import generics
from .models import AverageSpeed, Segment, Location
from .serializers import LocationSerializer, SegmentSerializer, SpeedSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.gis.geos import Point


# ---------------------------------------------------- CRUD for Locations with IDs
class LocationCreateApi(generics.CreateAPIView):
  queryset = Segment.objects.all()
  serializer_class = LocationSerializer


class LocationListApi(generics.ListAPIView):
  queryset = Segment.objects.all()
  serializer_class = LocationSerializer


class LocationUpdateApi(generics.RetrieveUpdateAPIView):
  queryset = Segment.objects.all()
  serializer_class = LocationSerializer


class LocationDeleteApi(generics.DestroyAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer


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


# ---------------------------------------------------- Crud for AverageSpeed Given Segment ID
class SpeedBySegListApi(generics.ListAPIView):
  serializer_class = SpeedSerializer

  def get_queryset(self):
    seg_id = int(self.kwargs['segment_id'])
    print("Seg id is: ", seg_id)
    return AverageSpeed.objects.filter(segment = seg_id)


# ---------------------------------------------------- Main for Segment Given Segment Location (WIP)
class SegmentByLocCreateApi(generics.CreateAPIView):
  queryset = Segment.objects.all()
  serializer_class = SegmentSerializer
  """
  View for creating a model instance given the start and end location
  of a segment. Will create new locations if not found
  """
  def post(self, request, *args, **kwargs):
    post = dict(request.POST.items())
    print("post items: ", post)
    if "start_long" not in post and "start_lat" not in post \
       and "end_long" not in post and "end_lat" not in post:
      print("invalid start and end value")
      return Response(status=status.HTTP_409_CONFLICT)  # Todo improve, not the best error handling
    return self.create(request, *args, **kwargs)

  def create(self, request):
    start_long = float(request.data['start_long'][0])  # Todo there are better ways to do it
    start_lat = float(request.data['start_lat'][0])
    end_long = float(request.data['end_long'][0])
    end_lat = float(request.data['end_lat'][0])
    start_p = Point(start_long, start_lat)
    end_p = Point(end_long, end_lat)
      
    [start, end] = Location.objects.bulk_create([
        Location(point=start_p),
        Location(point=end_p)
      ]
      ,ignore_conflicts=True)

    ## TODO not enough time to implementi this

    #loc_serializer = LocationSerializer(start)
    #if loc_serializer.is_valid():
      #loc_serializer.save()

    #print("start: ", start_p)

    #print("end: ", end_p)
    #start, start_created = Location.objects.get_or_create(defaults={'point': start_p})
    #print("Start point created: ", start_created)

    #end, end_created = Location.objects.get_or_create(defaults={'point': end_p})
    #print("End point created: ", end_created)
    #print("start: ", start, " end: ", end)
    segment = Segment.objects.create(start=start, end=end)
    serializer = SegmentSerializer(segment, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #serializer = self.get_serializer(data=request.data)
    #serializer.is_valid(raise_exception=True)
    #self.perform_create(serializer)
    #headers = self.get_success_headers(serializer.data)
    #return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    #task = self.get_object(pk)
    #serializer = TaskSerializer(task, data=request.data, partial=True) # set partial=True to update a data partially