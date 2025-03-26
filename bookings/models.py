from django.db import models
from users.models import CustomUser

class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    destination = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    hotel_name = models.CharField(max_length=255, null=True, blank=True)
    car_rental = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.destination}"
