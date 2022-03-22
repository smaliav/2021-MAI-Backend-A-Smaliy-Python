from django.urls import path, include


urlpatterns = [
    path('profile/', include('core.profile_urls')),   # Profile
    path('car/', include('core.car_urls')),           # Car
    path('category/', include('core.category_urls'))  # Category
]
