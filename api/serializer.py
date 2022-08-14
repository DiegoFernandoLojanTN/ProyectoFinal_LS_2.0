from dataclasses import field
from rest_framework import serializers
from eventos.models import Evento, Orden

class EventoSerialize(serializers.ModelSerializer):
    class Meta:
        model =Evento
        fields = '__all__'

class OrdenSerialize(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'
