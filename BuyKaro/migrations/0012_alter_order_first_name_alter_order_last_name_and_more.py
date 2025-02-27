# Generated by Django 3.2.5 on 2024-07-20 08:18

from django.db import migrations, models
import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('BuyKaro', '0007_remove_order_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=100, default="Unknown"),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=100, default="Unknown"),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(default="", max_length=254),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default="000-000-0000", max_length=15),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(max_digits=10, decimal_places=2, default=0.00),
        ),
    ]
