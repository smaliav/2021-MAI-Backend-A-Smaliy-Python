from django.urls import path
from .views import *


urlpatterns = [
    path('<int:user_id>/', get_user_by_id, name="get_user_by_id"),
    path('<int:user_id>/advert/', post_advert, name="post_advert"),
]
