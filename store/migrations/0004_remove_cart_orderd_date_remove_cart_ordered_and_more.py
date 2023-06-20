# Generated by Django 4.2.1 on 2023-06-15 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_order_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='orderd_date',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='ordered',
        ),
        migrations.AddField(
            model_name='order',
            name='orderd_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]