from django.urls import path
from .views import events_api, orders_api
urlpatterns = [
    path('eventos/', events_api, name="evento"),
    path('orders/', orders_api, name="orders")
]
