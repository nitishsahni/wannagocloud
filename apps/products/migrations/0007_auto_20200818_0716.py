# Generated by Django 3.1 on 2020-08-18 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_subscriptions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='riserva',
            old_name='per_month',
            new_name='selling_price',
        ),
    ]
