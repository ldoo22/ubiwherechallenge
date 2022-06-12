from django.urls import path
from .views import *


urlpatterns = [
    path('segment', SegmentListApi.as_view()),
    path('segment/create', SegmentCreateApi.as_view()),
    path('segment/<int:pk>', SegmentUpdateApi.as_view()),
    path('segment/<int:pk>/delete', SegmentDeleteApi.as_view()),

    path('asm', SpeedListApi.as_view()),  # asm <=> average speed meassure
    path('asm/create', SpeedCreateApi.as_view()),
    path('asm/<int:pk>', SpeedUpdateApi.as_view()),
    path('asm/<int:pk>/delete', SpeedDeleteApi.as_view()),
]