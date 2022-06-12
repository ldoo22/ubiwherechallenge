from django.contrib import admin
from .models import *

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
  list_display = ['point']

@admin.register(Segment)
class SegmentAdmin(admin.ModelAdmin):
  list_display = ['start', 'end']

@admin.register(AverageSpeed)
class SegmentAdmin(admin.ModelAdmin):
  list_display = ['average_speed', 'intensity', 'characterization', 'segment']