from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='venue_images')
    address = models.CharField(max_length=45)
    website = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

class Guest(models.Model):
    name = models.TextField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    status = models.CharField(
        max_length=10,
        choices=[("Yes", "Yes"), ("No", "No"), ("Pending", "Pending")],
        default="Pending",
    )

    def __str__(self):
        return self.name


class Wedding(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField()
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField()
    venue = models.ForeignKey(Venue, on_delete=models.RESTRICT)
    guests = models.ManyToManyField(Guest)

    def __str__(self):
        return self.title