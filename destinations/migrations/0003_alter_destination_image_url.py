# Generated by Django 5.0.6 on 2024-05-20 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0002_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='image_url',
            field=models.URLField(max_length=1000),
        ),
    ]
