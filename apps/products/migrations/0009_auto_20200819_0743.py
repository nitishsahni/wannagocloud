# Generated by Django 3.1 on 2020-08-19 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200819_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draas',
            name='cost_price',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name='draas',
            name='selling_price',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name='iaas',
            name='cost_price',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name='iaas',
            name='selling_price',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='selling_price',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
    ]