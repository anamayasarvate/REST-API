from django.contrib import admin
from .models import Customer, Executive, CustomerType

admin.site.register(Customer)
admin.site.register(CustomerType)
admin.site.register(Executive)