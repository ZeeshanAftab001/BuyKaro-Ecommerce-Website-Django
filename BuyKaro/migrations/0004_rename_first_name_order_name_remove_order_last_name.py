# Generated by Django 5.0.6 on 2024-07-23 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BuyKaro', '0003_delete_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
    ]
