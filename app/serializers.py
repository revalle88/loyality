from rest_framework import serializers
from .models import Customer, Order

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('card', 'first_name','last_name', 'patronymic', 'bdate', 'phone', 'city', 'street', 'email', 'summ')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('card', 'date', 'check', 'summ')
