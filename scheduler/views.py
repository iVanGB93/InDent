from django.shortcuts import redirect, render

from .forms import AppointmentForm
from .models import Appointment, Day
from datetime import datetime

def calendar(request):
    days = Day.objects.all()
    appointments = Appointment.objects.all()
    content = {'days': days, 'appointments': appointments}
    return render(request, 'scheduler/index.html', content)

def dayDetail(request, pk):
    if Day.objects.filter(date=datetime(2022, 11, pk)).exists():
        day = Day.objects.get(date=datetime(2022, 11, pk))
        print("exist")
    else:
        day = Day(date=datetime(2022, 11, pk))
        print("created", day)
        day.save()
    appointments = Appointment.objects.filter(day=day.pk)
    content = {'day': day, 'appointments': appointments}
    return render(request, 'scheduler/dayDetail.html', content)

def newAppointment(request):
    form = AppointmentForm
    content = {'form': form}
    if request.method == 'POST':
        appointment = form(request.POST)
        if appointment.is_valid():
            appointment.save()
        print(request)
        return redirect('scheduler:dayDetail', 1)
    return render(request, 'scheduler/newAppointment.html', content)
