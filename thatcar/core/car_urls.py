from django.urls import path
from .views import *


urlpatterns = [
    path('<int:car_id>/', get_car, name="get_car"),    # Get Car
    path('all/', get_cars, name="get_cars"),           # Get Car List
]
