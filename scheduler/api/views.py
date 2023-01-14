from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from scheduler.api.serializers import YearSerializer, MonthSerializer, DaySerializer, AppointmentSerializer
from scheduler.models import Year, Month, Day, Appointment

class YearView(APIView):

    def get(self, queryset=None, **kwargs):
        year = self.kwargs.get('pk')
        if Year.objects.filter(pk=year).exists():
            year = Year.objects.filter(pk=year)
            serializer = YearSerializer(year)
            print(serializer)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            year = Year()
            year.save()
            serializer = YearSerializer(year)
            print(serializer)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

class DayView(APIView):

    def get(self, queryset=None, **kwargs):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        if Year.objects.filter(year=year).exists():
            year = Year.objects.get(year=year)
        else:
            year = Year(year=year)
            year.save()
        if Month.objects.filter(year=year, month=month).exists():
            month = Month.objects.get(year=year, month=month)
        else:
            month = Month(year=year, month=month)
            month.save()
        if Day.objects.filter(month=month, day=day).exists():
            day = Day.objects.get(month=month, day=day)
            objects = Appointment.objects.filter(day=day)
            appointments = []
            for i in objects:
                serializer = AppointmentSerializer(i)
                appointments.append(serializer.data)
            return Response(data=appointments, status=status.HTTP_200_OK)
        else:
            day = Day(month=month, day=day)
            day.save()
            objects = Appointment.objects.filter(day=day)
            appointments = []
            for i in objects:
                serializer = AppointmentSerializer(i)
                appointments.append(serializer.data)
            return Response(data=appointments, status=status.HTTP_200_OK)
            #return Response(data={'message': 'sorry, not found'}, status=status.HTTP_404_NOT_FOUND)