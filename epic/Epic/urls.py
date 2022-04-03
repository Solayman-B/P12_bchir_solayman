from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Account.views import ClientViewset
from Contract.views import ContractViewset
from Event.views import EventViewset


router = routers.SimpleRouter()

router.register('client', ClientViewset, basename='client')
router.register('event', EventViewset, basename='event')
router.register('contract', ContractViewset, basename='contract')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
