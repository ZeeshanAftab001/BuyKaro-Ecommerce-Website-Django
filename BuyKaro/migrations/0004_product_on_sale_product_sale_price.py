# Generated by Django 5.0.6 on 2024-07-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BuyKaro', '0003_alter_catagory_options_catagory_image_cat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='on_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.IntegerField(default=0),
        ),
    ]
