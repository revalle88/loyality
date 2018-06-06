from django.urls import path
from . import views
from rest_framework import routers
from app.views import CustomerViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)


urlpatterns = router.urls
#urlpatterns = [
	#path('', views.index, name='index'),
#]

