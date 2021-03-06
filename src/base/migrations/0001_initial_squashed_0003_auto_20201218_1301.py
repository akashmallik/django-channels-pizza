# Generated by Django 3.1.4 on 2020-12-18 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('base', '0001_initial'), ('base', '0002_auto_20201218_0603'), ('base', '0003_auto_20201218_1301')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='pizzas')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(editable=False, max_length=10, unique=True)),
                ('amount', models.IntegerField()),
                ('status', models.CharField(choices=[('Order Received', 'Order Received'), ('Baking', 'Baking'), ('Baked', 'Baked'), ('Out for Delivery', 'Out for Delivery'), ('Order Delivered', 'Order Delivered')], default='Order Received', max_length=25)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.pizza')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
