from django.db import models
from django.contrib.auth.models import User
from item.models import Product

# Create your models here.

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s favorite: {self.product.name}"
    