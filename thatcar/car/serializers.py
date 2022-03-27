from rest_framework import serializers
from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarColor
        fields = '__all__'


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCategory
        fields = "__all__"
