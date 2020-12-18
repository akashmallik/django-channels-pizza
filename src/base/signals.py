import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order


@receiver(post_save, sender=Order)
def order_status(sender, instance, created, **kwargs):

    if not created:
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

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'order_%s' % instance.order_id, {
                'type': 'order_status',
                'values': json.dumps(data)
            }
        )
