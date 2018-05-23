from django.shortcuts import render

from django.http import HttpResponse

from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer





def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
