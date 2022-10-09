from django.db import models

class Solar(models.Model):
    Province = models.CharField(max_length = 180)
    usage = models.CharField(max_length = 180)
    rainFallType = models.CharField(max_length = 180)
    skyType = models.CharField(max_length = 180)
    windDirection = models.CharField(max_length = 180)
    windSpeed = models.CharField(max_length = 180)
    humidity = models.CharField(max_length = 180)
    Temperature = models.CharField(max_length = 180)
    elevation = models.CharField(max_length = 180)
    radiation = models.CharField(max_length = 180)
    VaporPressure = models.CharField(max_length = 180)
    surfaceTemperature = models.CharField(max_length = 180)
    AtmospherePressure= models.CharField(max_length = 180)
    Bulbs = models.CharField(max_length = 180)
    Fan = models.CharField(max_length = 180)
    Iron = models.CharField(max_length = 180)
    TV = models.CharField(max_length = 180)
    Refrigerator = models.CharField(max_length = 180)
    Blender = models.CharField(max_length = 180)
    airConditioner = models.CharField(max_length = 180)
    waterHeater = models.CharField(max_length = 180)
    microwaveOven = models.CharField(max_length = 180)
    riceCooker = models.CharField(max_length = 180)

    def __str__(self):
        return self.Province
