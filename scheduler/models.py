from django.db import models
from django.contrib.auth.models import User
import datetime

class Year(models.Model):
    year = models.IntegerField(default=datetime.datetime.now().year, unique=True)

    def __str__(self):
        return 'Year ' + str(self.year)

class Month(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    month = models.IntegerField(default=datetime.datetime.now().month)

    def __str__(self):
        return 'Year ' + str(self.year.year) + ', Month ' + str(self.month)

class Day(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    day = models.IntegerField(default=datetime.datetime.now().day)

    def __str__(self):
        return 'Year ' + str(self.month.year.year) + ', Month ' + str(self.month.month) + ', Day ' + str(self.day)

class Appointment(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    time = models.TimeField()
    duration = models.IntegerField(default=15)
    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='provider')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient')
    topic = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    confirmed = models.BooleanField(default=False)
    arrived = models.BooleanField(default=False)
    chair = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)

    def __str__(self):
        return str(self.day.month.year.year) + '/' + str(self.day.month.month) + '/' + str(self.day.day) + ' (' + str(self.time) + '): ' + self.patient.username + ' ' + self.topic