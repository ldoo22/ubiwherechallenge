from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class Location(models.Model):
  """
  Information about a particular location
  """
  point = models.PointField(geography=True, default=Point(0.0, 0.0))

  def __str__(self):
    return "(" + str(self.point.x) + ", " + str(self.point.y) + ")"


class Segment(models.Model):
  """
  Information about a segment composed of a start location and a end location
  """
  start = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="start")
  end = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="end")

  def __str__(self):
    return str(self.start) + " -> " + str(self.end)