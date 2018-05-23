from django.urls import path
from . import views
from rest_framework import routers
from app.views import CustomerViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)


urlpatterns = router.urls
#urlpatterns = [
	#path('', views.index, name='index'),
#]

