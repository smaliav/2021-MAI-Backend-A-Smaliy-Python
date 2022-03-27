from django.urls import path, include


urlpatterns = [
    path('cars/', include('car.urls')),        # Car
    path('users/', include('user.urls')),      # User
    path('adverts/', include('advert.urls')),  # Adverts
]
