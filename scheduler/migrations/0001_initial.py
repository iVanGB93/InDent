# Generated by Django 4.1.2 on 2023-01-14 16:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2023, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(default=1)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.year')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(default=14)),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.month')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 1, 14, 11, 54, 39, 56348))),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.day')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]