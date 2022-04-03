from rest_framework import serializers

from core import models

class listbankSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.listbanks
        fields = '__all__'

