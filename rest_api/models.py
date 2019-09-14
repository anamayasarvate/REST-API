from django.db import models

class CustomerType(models.Model):
	customer_type = models.CharField(max_length = 50)

	def __str__(self):
		return self.customer_type

class Customer(models.Model):
	name = models.CharField(max_length = 50)
	age = models.PositiveIntegerField(default = 22)
	customer_type = models.ForeignKey(CustomerType, on_delete = models.SET_NULL, null = True)

	def __str__(self):
		return self.name

class Executive(models.Model):
	name = models.CharField(max_length = 50)
	customers = models.ManyToManyField(Customer) 

	def __str__(self):
		return self.name