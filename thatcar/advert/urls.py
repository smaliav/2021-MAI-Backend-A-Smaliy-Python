from django.urls import path
from .views import *


urlpatterns = [
    path('', post_advert, name="post_advert"),
    path('all/', get_all_adverts, name="get_all_adverts"),
    path('<int:advert_id>/', get_advert_by_id, name="get_advert_by_id"),
    path('color/<int:color_id>', get_adverts_by_color_id, name="get_adverts_by_color_id"),
]
