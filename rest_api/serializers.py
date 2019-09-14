from rest_framework import serializers
from .models import Customer, Executive, CustomerType

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta():
		model = Customer
		fields = ["id", "name", "age", "customer_type", "url"]

class CustomerTypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta():
		model = CustomerType
		fields = ["id", "customer_type", "url"]

class ExecutiveSerializer(serializers.HyperlinkedModelSerializer):
	class Meta():
		model = Executive
		fields = ["id", "name", "customers" ,"url"]