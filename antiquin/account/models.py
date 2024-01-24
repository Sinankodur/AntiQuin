from django.db import models


class Address(models.Model):
    address_line = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.address_line}, {self.city}, {self.state} {self.pin_code}"
