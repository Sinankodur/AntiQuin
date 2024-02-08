from django.contrib.auth.models import User
from django.db import models
from item.models import Product

class Order(models.Model):
    ORDERED = 'ordered'
    DISPATCHED = 'dispatched'
    SHIPPED = 'shipped'

    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (DISPATCHED, 'Dispatched'),
        (SHIPPED, 'Shipped')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    pincode = models.IntegerField()
    place = models.CharField(max_length=100)
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_cancelled = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)

    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

    def calculate_total(self):
        total = sum(item.calculate_subtotal() for item in self.orderitem_set.all())
        return total
    
    def mark_as_delivered(self):
        if not self.is_delivered:
           self.is_delivered = True
           self.status = Order.DISPATCHED
           self.save()

    def __str__(self):
        return f"Order ID #{self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_subtotal(self):
        if self.product and self.quantity:
            self.subtotal = self.product.price * self.quantity
            return self.subtotal
        return 0

    def save_sub(self, *args, **kwargs):
        self.calculate_subtotal()
        super().save(*args, **kwargs)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} x {self.quantity} - Order #{self.order.id}"
    

