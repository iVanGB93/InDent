from scheduler.api.views import DayView
from django.urls import path

app_name='scheduler-api'

urlpatterns = [
    path('<str:year>/<str:month>/<str:day>/', DayView.as_view(), name="days"),
]