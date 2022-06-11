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