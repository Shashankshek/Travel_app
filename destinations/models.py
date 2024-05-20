from django.db import models

# Create your models here.


class Destination(models.Model):
    CATEGORY_CHOICES = [
        ('Beach', 'Beach'),
        ('Mountain', 'Mountain'),
        ('City', 'City'),
        ('Historical', 'Historical'),
    ]

    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    description = models.TextField()
    best_time_to_visit = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image_url = models.URLField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    travel_date = models.DateField()
    num_of_people = models.PositiveIntegerField()

    def __str__(self):
        return f"Booking by {self.user} for {self.destination.name} on {self.travel_date}"
