from django.urls import path
from .views import *

urlpatterns = [
    path('<int:advert_id>/', get_advert_by_id, name="get_advert_by_id"),
    path('color/<int:color_id>', get_adverts_by_color_id, name="get_adverts_by_color_id"),
]
