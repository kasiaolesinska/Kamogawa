from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    year_of_birth = models.IntegerField()


class Boxer(Person):
    class WeightCategory(models.TextChoices):
        FEATHER = 'feather'
        LIGHT = 'light'
        MIDDLE = 'middle'
        HEAVY_LIGHT = 'heavy light'
        SUPER_HEAVY = 'super heavy'

    weight_category = models.CharField(blank=False, max_length=30, default=WeightCategory.MIDDLE, choices=WeightCategory.choices)
    fights_total = models.IntegerField()
    fights_won = models.IntegerField()


class Staff(Person):
    role = models.CharField(max_length=25)
