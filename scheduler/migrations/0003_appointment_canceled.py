# Generated by Django 4.1.2 on 2023-01-14 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_appointment_arrived_appointment_chair_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='canceled',
            field=models.BooleanField(default=False),
        ),
    ]
