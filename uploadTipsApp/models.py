from django.db import models

class File(models.Model):
    noOfMembers = models.IntegerField()
    noOofTimesUsingTheIron = models.IntegerField()
    noOfTimesUsingTheWashingMachine =models.IntegerField()
    firstmonthUnits = models.IntegerField()
    secondMonthUnits = models.IntegerField()
    thirdMonthUnits = models.IntegerField()
    firstMonthCost  = models.FloatField()
    secondMonthCost  = models.FloatField()
    thirdMonthCost = models.FloatField()
    averageUnits = models.FloatField()
    microwave_Yes = models.IntegerField()
    hairDryer_Yes = models.IntegerField()
    electricOven_Yes = models.IntegerField()
    windowType_Yes = models.IntegerField()
    waterGeyser_Yes = models.IntegerField()
    electricWaterHeater_Yes = models.IntegerField()
    cielingFan_Yes = models.IntegerField()
    standFan_Yes = models.IntegerField()
    tableFan_Yes = models.IntegerField()
    exhaustFan_Yes = models.IntegerField()

    