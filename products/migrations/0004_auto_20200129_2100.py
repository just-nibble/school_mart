# Generated by Django 2.2.7 on 2020-01-29 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200129_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='buy',
            new_name='category',
        ),
    ]
