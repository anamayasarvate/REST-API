from django.urls import path, include
from rest_framework import routers
from .views import CustomerView,  ExecutiveView, CustomerTypeView

router = routers.DefaultRouter()
router.register("customers", CustomerView)
router.register("customer-types", CustomerTypeView)
router.register("executives", ExecutiveView)


urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls'))
]
