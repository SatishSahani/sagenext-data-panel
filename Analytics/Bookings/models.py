from django.db import models



# Create your models here.
class BookingsData(models.Model):
    month = models.CharField(max_length=20)
    impression = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    conversions = models.DecimalField(max_digits=10, decimal_places=2)
    bookings = models.PositiveIntegerField()

    def __str__(self):
        return self.month