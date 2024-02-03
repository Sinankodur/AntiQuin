from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    is_sold = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1) 
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('created_at',)

    def __str__(self):
        return self.name
