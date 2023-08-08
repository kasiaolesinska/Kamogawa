from django.db import models
from django.urls import reverse


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    year_of_birth = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Boxer(Person):
    class WeightCategory(models.TextChoices):
        FEATHER = 'feather'
        LIGHT = 'light'
        MIDDLE = 'middle'
        HEAVY_LIGHT = 'heavy light'
        SUPER_HEAVY = 'super heavy'

    weight_category = models.CharField(blank=False, max_length=30, default=WeightCategory.MIDDLE,
                                       choices=WeightCategory.choices)
    fights_total = models.IntegerField()
    fights_won = models.IntegerField()

    def get_absolute_url(self):
        return reverse('boxer-detail', kwargs={'pk': self.pk})


class Staff(Person):
    role = models.CharField(max_length=25)

    def get_absolute_url(self):
        return reverse('staff-detail', kwargs={'pk': self.pk})
