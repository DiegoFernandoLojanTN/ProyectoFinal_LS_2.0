from django.urls import path
from .views import *


urlpatterns = [
    path('', EventosListView.as_view(), name = 'list'),
    path('<int:pk>/', EventosDetailView.as_view(), name = 'detail'),
    path('<int:pk>/checkout/', EventosCheckoutView.as_view(), name = 'checkout'),
    path('complete/', paymentComplete, name = 'complete'),
    path('search/', SearchResultsListView.as_view(), name = 'search_results'),
    path('qr/', verQr.as_view(), name = 'verQr'),
]