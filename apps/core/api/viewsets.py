import imp
from rest_framework import viewsets
from core.api import serializers
from core import models

class listbanksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.listbankSerializer
    queryset = models.listbanks.objects.all()