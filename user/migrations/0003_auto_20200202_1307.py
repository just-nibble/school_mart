# Generated by Django 2.2.7 on 2020-02-02 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200202_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, height_field=200, upload_to='products/%Y/$m/$d', width_field=200),
        ),
    ]