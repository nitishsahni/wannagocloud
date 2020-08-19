# Generated by Django 3.1 on 2020-08-16 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Riserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('price_dollars', models.IntegerField()),
                ('price_aed', models.IntegerField()),
                ('per_month', models.IntegerField()),
            ],
        ),
    ]