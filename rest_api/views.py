from django.shortcuts import render
from .models import Customer, Executive, CustomerType
from .serializers import CustomerSerializer, ExecutiveSerializer, CustomerTypeSerializer
from rest_framework import viewsets, permissions

class CustomerView(viewsets.ModelViewSet):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class CustomerTypeView(viewsets.ModelViewSet):
	queryset = CustomerType.objects.all()
	serializer_class = CustomerTypeSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ExecutiveView(viewsets.ModelViewSet):
	queryset = Executive.objects.all()
	serializer_class = ExecutiveSerializer
