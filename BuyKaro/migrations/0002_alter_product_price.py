# Generated by Django 5.0.6 on 2024-07-17 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BuyKaro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, max_length=6),
        ),
    ]
