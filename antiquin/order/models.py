from django.contrib.auth.models import User
from django.db import models
from item.models import Product


class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'

    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    pincode = models.CharField(max_length=20)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    is_cancelled = models.BooleanField(default=False)

    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


    def calculate_subtotal(self):
        if self.product and self.quantity:
            self.subtotal = self.product.price * self.quantity
            return self.subtotal
        return 0

    def save(self, *args, **kwargs):
        self.calculate_subtotal()
        super().save(*args, **kwargs)

    def calculate_order_total(self):
        total = sum(item.subtotal for item in self.orderitem_set.all())
        return total
 
    def save(self, *args, **kwargs):
        self.order_total = self.calculate_order_total()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.quantity} x {self.product.name} for Order #{self.order.id}"
