# Generated by Django 4.2.7 on 2024-02-05 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_remove_orderitem_order_total_alter_order_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ordered', 'Ordered'), ('dispatched', 'Dispatched')], default='ordered', max_length=20),
        ),
    ]
