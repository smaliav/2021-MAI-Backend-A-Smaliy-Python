from rest_framework import viewsets

from .models import Advert
from .serializers import AdvertSerializer


class AdvertViewSet(viewsets.ModelViewSet):
    queryset = Advert.objects.all().order_by('id')
    serializer_class = AdvertSerializer
