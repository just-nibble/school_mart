# Generated by Django 2.2.7 on 2020-02-02 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='category',
            field=models.CharField(choices=[('elec', 'electronics'), ('veh', 'vehicles'), ('fash', 'fashion'), ('home', 'home_appliance')], max_length=20),
        ),
    ]
