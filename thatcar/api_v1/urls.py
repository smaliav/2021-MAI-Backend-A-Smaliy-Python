from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('car/', include('car.urls')),        # Car
    path('user/', include('user.urls')),      # User
    path('advert/', include('advert.urls')),  # User
]
