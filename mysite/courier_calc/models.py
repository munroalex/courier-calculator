from django.db import models

# List of locations and whether or not they can be an origin and/or destination
class Locations(models.Model):
    location = models.CharField(max_length=300)
    origin = models.BooleanField(default=True)
    destination = models.BooleanField(default=True)

    def __str__(self):
         return self.location
# For future use when different routes require different rate calculations
class Routes(models.Model):
    origin = models.CharField(max_length=300)
    destination = models.CharField(max_length=300)
    base_rate = models.IntegerField(default=5000000)
    per_m3 = models.IntegerField(default=650)
    collateral_perc = models.FloatField(default=0.02)