from django.shortcuts import render 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import *
from django.urls import reverse_lazy
from django.db.models import Q # for search method
from django.http import JsonResponse
import json

class EventosListView(ListView):
    model = Evento
    template_name = 'list.html'

class EventosDetailView(DetailView):
    model = Evento
    template_name = 'detail.html'


class SearchResultsListView(ListView):
	model = Evento
	template_name = 'search_results.html'

	def get_queryset(self): # new
		query = self.request.GET.get('q')
		return Evento.objects.filter(
		Q(nombre__icontains=query) | Q(artista__icontains=query)
		)

class EventosCheckoutView(LoginRequiredMixin, DetailView):
    model = Evento
    template_name = 'checkout.html'
    login_url     = 'login'


def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)
	product = Evento.objects.get(id=body['productId'])
	Orden.objects.create(
		product=product
	)
	return JsonResponse('Pago Completado!', safe=False)

################################

class verQr(ListView):
	model = Evento
	template_name = 'codigoQr.html'

	