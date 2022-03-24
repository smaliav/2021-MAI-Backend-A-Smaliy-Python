from django.urls import path
from .views import *


urlpatterns = [
    path('<int:car_id>/', get_car_by_id, name="get_car_by_id"),
    path('brand/<str:brand_name>/', get_cars_by_brand_name, name="get_cars_by_brand"),
    path('category/<str:category_id>/', get_cars_by_category_id, name="get_cars_by_category_id"),
]
