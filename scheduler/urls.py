from django.urls import path
from . import views

app_name='scheduler'

urlpatterns = [
    path('', views.calendar, name='scheduler'),
    path('<int:pk>/', views.dayDetail, name='dayDetail'),
    path('new/', views.newAppointment, name='newAppointment'),
]