from django.db import models
from django.utils import timezone

# Create your models here.
class CustomerForm(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    mobile_number = models.IntegerField(max_length=10)
    address = models.CharField(max_length=200)
    room_no = models.PositiveIntegerField(unique = True)
    no_of_the_days_to_stay = models.PositiveIntegerField()
    date = models.DateField(default=timezone.now)

