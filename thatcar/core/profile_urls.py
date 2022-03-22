from django.urls import path
from .views import *


urlpatterns = [
    path('<int:profile_id>/', get_profile, name="get_profile"),  # Get User Profile
]
