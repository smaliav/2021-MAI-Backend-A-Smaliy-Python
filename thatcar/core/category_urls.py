from django.urls import path
from .views import *


urlpatterns = [
    path('<str:category>/', get_category, name="get_category")  # Get category
]
