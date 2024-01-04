from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    prd_img = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name
    