from django.urls import path
from .views import *


urlpatterns = [
    path('segment', SegmentListApi.as_view()),
    path('segment/create', SegmentCreateApi.as_view()),
    path('segment/<int:pk>', SegmentUpdateApi.as_view()),
    path('segment/<int:pk>/delete', SegmentDeleteApi.as_view()),
]