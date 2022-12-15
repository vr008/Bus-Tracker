from concurrent.futures.process import _python_exit
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class User(AbstractUser):
    choices = (
    ('bus', 'Day Scholor'),
    ('hos', 'Hosteller'),
    ('inc', 'Transport department'),
    )
    user_type = models.CharField(max_length=3, choices=choices, default='bus', null=False, blank=False)

    def __str__(self):
        return f"{self.username} - {self.user_type}"


class Announcements(models.Model):
    title = models.CharField(max_length=100)
    choices = (
        ('bus', 'Bus'),
        ('hos', 'Hostel'),
    )
    for_user = models.CharField(max_length=3, choices=choices, default='bus', null=False, blank=False)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.date}"
class Feedback(models.Model):
    title = models.CharField(max_length=100)
    choices = (
        ('bus', 'Bus'),
        ('hos', 'Hostel'),
    )
    for_user = models.CharField(max_length=3, choices=choices, default='bus', null=False, blank=False)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.date}"

class Stops(models.Model):
    stop_no = models.IntegerField(primary_key=True)
    stop_name = models.CharField(max_length=100)
    stop_lat = models.FloatField(null=True, blank=True)
    stop_lng = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.stop_no} - {self.stop_name}"

class Route(models.Model):
    route_no = models.IntegerField(primary_key=True)
    waypoints = models.ManyToManyField(Stops, related_name="routes")
    start_stop = models.ForeignKey(Stops, on_delete=models.CASCADE, related_name="start_stop", null=False)


    def __str__(self):
        return f"Route {self.route_no}"

class Bus(models.Model):
    bus_no = models.IntegerField(primary_key=True)
    bus_route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="buses")
    capacity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(60)], default=60)

    def __str__(self):
        return f"Bus {self.bus_no}"

class BusCoordinates(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name="bus_coordinates")
    latitude = models.FloatField()
    longitude = models.FloatField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bus.bus_no} - {self.date}"

class Bookings(models.Model):
    users = models.ManyToManyField(User, limit_choices_to={'user_type': 'hos'}, related_name="bookings", blank=True, null=True)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name="bookings")
    date = models.DateField()
    time = models.TimeField(default='00:00:00')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="bookings")
    bus_capacity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(60)], default=60)

    def __str__(self):
        return f"{self.bus} - {self.date}"