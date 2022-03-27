from rest_framework import viewsets

from .serializers import *


class CarColorViewSet(viewsets.ModelViewSet):
    queryset = CarColor.objects.all().order_by('id')
    serializer_class = CarColorSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('id')
    serializer_class = CarSerializer


class CarBrandViewSet(viewsets.ModelViewSet):
    queryset = CarBrand.objects.all().order_by('id')
    serializer_class = CarBrandSerializer


class CarCategoryViewSet(viewsets.ModelViewSet):
    queryset = CarCategory.objects.all().order_by('id')
    serializer_class = CarCategorySerializer
