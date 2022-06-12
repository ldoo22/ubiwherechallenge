from django.urls import path
from .views import *


urlpatterns = [
    path('location', LocationListApi.as_view()),
    path('location/create', LocationCreateApi.as_view()),
    path('location/<int:pk>', LocationUpdateApi.as_view()),
    path('location/<int:pk>/delete', LocationDeleteApi.as_view()),

    path('segment', SegmentListApi.as_view()),
    path('segment/create', SegmentCreateApi.as_view()),
    path('segment/<int:pk>', SegmentUpdateApi.as_view()),
    path('segment/<int:pk>/delete', SegmentDeleteApi.as_view()),

    path('asm', SpeedListApi.as_view()),  # asm <=> average speed meassure
    path('asm/create', SpeedCreateApi.as_view()),
    path('asm/<int:pk>', SpeedUpdateApi.as_view()),
    path('asm/<int:pk>/delete', SpeedDeleteApi.as_view()),

    path('asm-by-segm/<int:segment_id>', SpeedBySegListApi.as_view()),  # asma-by-segm <=> average speed meassure by segment

    path('segment-by-loc/create', SegmentByLocCreateApi.as_view()),
]