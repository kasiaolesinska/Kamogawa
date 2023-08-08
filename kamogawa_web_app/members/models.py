from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.IntegerField()


class Boxer(Person):
    class WeightCategory:
        FEATHER = 'feather'
        LIGHT = 'light'
        MIDDLE = 'middle'
        HEAVY_LIGHT = 'heavy light'
        SUPER_HEAVY = 'super heavy'

    weight_category = models.TextChoices(names=WeightCategory)
    fights_total = models.IntegerField()
    fights_lost = models.IntegerField()


class Staff(Person):
    role = models.CharField(max_length=25)
