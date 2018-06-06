from django.shortcuts import render

from django.http import HttpResponse

from rest_framework import viewsets
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'card'

class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	lookup_field = 'card'
	def perform_create(self, serializer):
		card = self.request.data['card']
		customer = Customer.objects.get(card=card)
		serializer.save(customer=customer)




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
