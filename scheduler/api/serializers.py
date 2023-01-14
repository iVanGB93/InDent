from rest_framework import serializers

from scheduler.models import Year, Month, Day, Appointment

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ('__all__')

class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = ('__all__')

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ['day',]

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('__all__')
