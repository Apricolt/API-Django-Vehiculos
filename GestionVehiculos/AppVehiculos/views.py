import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from AppVehiculos.models import vehiculo
from .serializer import vehiculo_serializer

# Create your views here.

class VehiculoApiView(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            'placa': request.data.get('placa'),
            'marca': request.data.get('marca'),
            'color': request.data.get('color'),
            'modelo': request.data.get('modelo'),
        }
        serializador = vehiculo_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status = status.HTTP_201_CREATED)
        
        return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        listas_vehiculos = vehiculo.objects.all()
        serializador_vehiculos = vehiculo_serializer(listas_vehiculos, many=True)
        return Response(serializador_vehiculos.data, status=status.HTTP_200_OK)
    
    def put(self, request, pkid):
        mivehiculo = vehiculo.objects.filter(id=pkid).update(
            placa = request.data.get('placa'),
            marca = request.data.get('marca'),
            color = request.data.get('color'),
            modelo = request.data.get('modelo')
        )
        return Response(status=status.HTTP_200_OK)
    
    def delete(self, request, pkid, *args, **kwargs):
        try:
            mivehiculo = vehiculo.objects.get(id=pkid)
            mivehiculo.delete()
            return Response({'message': 'Vehiculo eliminado'}, status=status.HTTP_204_NO_CONTENT)
        except vehiculo.DoesNotExist:
            return Response({'message': 'Vehiculo no encontrado'}, status=status.HTTP_404_NOT_FOUND)