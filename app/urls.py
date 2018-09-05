from django.urls import path
from . import views
from rest_framework import routers
from app.views import CustomerViewSet, OrderViewSet
from django.conf.urls import include, url

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)


#urlpatterns = router.urls
urlpatterns = [
	path('register/', views.index, name='index'),
]
urlpatterns += router.urls

#
#urlpatterns = [
#	url('^v1/', include(router.urls)),
#]

