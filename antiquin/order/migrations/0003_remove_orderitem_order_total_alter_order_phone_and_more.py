# Generated by Django 4.2.7 on 2024-01-28 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderitem_order_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order_total',
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='pincode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ordered', 'Ordered'), ('dispatched', 'dispatched')], default='ordered', max_length=20),
        ),
    ]
