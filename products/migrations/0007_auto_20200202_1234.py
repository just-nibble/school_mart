# Generated by Django 2.2.7 on 2020-02-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200202_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='catalogue',
            field=models.CharField(choices=[('elec', (('ph', 'phones'), ('tab', 'tablets'), ('acc', 'accessories'))), ('veh', (('ca', 'cars'), ('cyc', 'motorcycles')))], max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
