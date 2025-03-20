from AppVehiculos.models import vehiculo
from rest_framework import serializers

class vehiculo_serializer(serializers.ModelSerializer):
    class Meta:
        model = vehiculo
        fields = ['placa','marca','color','modelo']
        
        