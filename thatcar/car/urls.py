from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'colors', CarColorViewSet)
router.register(r'brands', CarBrandViewSet)
router.register(r'categories', CarCategoryViewSet)
router.register(r'', CarViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
