from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

class Location(models.Model):
  """
  Information about a particular location
  """
  point = models.PointField(geography=True, default=Point(0.0, 0.0), unique=True)

  def __str__(self):
    return "(" + str(self.point.x) + ", " + str(self.point.y) + ")"


class Segment(models.Model):
  """
  Information about a segment composed of a start location and a end location
  """
  start = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="start", default=None)
  end = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="end", default=None)

  def __str__(self):
    return str(self.start) + " -> " + str(self.end)

  class Meta:
    unique_together = ('start', 'end')


class AverageSpeed(models.Model):
  """
  Information about a average speed reading for a given segment
  """

  SPEED_LOW = 20
  SPEED_MODERATE = 50

  class Characterizations(models.TextChoices):
    HIGH = 'high', _('High')
    MODERATE = 'moderate', _('Moderate')
    LOW = 'low', _('Low')

  time = models.TimeField(auto_now_add=True)
  average_speed = models.FloatField()
  intensity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
  characterization = models.CharField(choices=Characterizations.choices, default=Characterizations.LOW, max_length=8)
  segment = models.ForeignKey(Segment, on_delete=models.CASCADE)

  def save(self, *args, **kwargs):
    if self.average_speed <= self.SPEED_LOW:
      print("Setting high inte")
      self.intensity = 2
      self.characterization = AverageSpeed.Characterizations.HIGH
    elif self.average_speed <= self.SPEED_MODERATE:
      print("Setting moderate inte")
      self.intensity = 1
      self.characterization = AverageSpeed.Characterizations.MODERATE
    else:
      print("Setting low inte")
      self.intensity = 0
      self.characterization = AverageSpeed.Characterizations.LOW

    super(AverageSpeed, self).save(*args, **kwargs)