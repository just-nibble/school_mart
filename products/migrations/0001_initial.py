# Generated by Django 2.2.7 on 2020-01-29 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('buy', models.CharField(choices=[('ele', 'electronics'), ('car', 'cars'), ('fsh', 'fashion'), ('sprt', 'sport'), ('home', 'home_appliance')], max_length=10)),
            ],
        ),
    ]