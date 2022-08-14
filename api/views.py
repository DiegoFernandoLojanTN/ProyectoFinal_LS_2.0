from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from eventos.models import Evento, Orden
from api.serializer import EventoSerialize,OrdenSerialize
from django.http import JsonResponse

@api_view(['GET'])
def events_api(request):
    list =  Evento.objects.all()
    list_serializer = EventoSerialize(list, many=True)
    return Response(list_serializer.data)

@api_view(['GET'])
def orders_api(request):
    list =  Orden.objects.all()
    array_events = []
    for i in list:
        print("===========")
        print(i.product.id)
        object = (Evento.objects.get(id=i.product.id))
        print(object.fecha)
        array_events.append(object)
        print("===========<<<<<<<<<<<<<,,")
    print(array_events)
    list_serializer = EventoSerialize(array_events, many=True)
    return Response(list_serializer.data)