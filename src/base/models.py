import string
import random

from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import get_object_or_404


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Pizza(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='pizzas')
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=10, unique=True, editable=False)
    amount = models.IntegerField()
    CHOICES = (
        ("Order Received", "Order Received"),
        ("Baking", "Baking"),
        ("Baked", "Baked"),
        ("Out for Delivery", "Out for Delivery"),
        ("Order Delivered", "Order Delivered"),
    )
    status = models.CharField(max_length=25, choices=CHOICES, default="Order Received")
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = random_string_generator()
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.order_id

    @staticmethod
    def get_order_details(order_id):
        instance = get_object_or_404(Order, order_id=order_id)

        progress_percentage = 0
        if instance.status == 'Order Received':
            progress_percentage = 20
        elif instance.status == 'Baking':
            progress_percentage = 40
        elif instance.status == 'Baked':
            progress_percentage = 60
        elif instance.status == 'Out for Delivery':
            progress_percentage = 80
        elif instance.status == 'Order Delivered':
            progress_percentage = 100

        data = {'order_id': instance.order_id, 'amount': instance.amount, 'status': instance.status,
                'date': str(instance.date), 'progress': progress_percentage}

        return data
