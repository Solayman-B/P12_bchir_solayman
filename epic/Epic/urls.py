from Account.views import TeamUserViewset, ClientViewset
from Contract.views import ContractViewset
from Event.views import EventViewset
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.SimpleRouter()

router.register("teamuser", TeamUserViewset, basename="teamuser")
router.register("client", ClientViewset, basename="client")
router.register("event", EventViewset, basename="event")
router.register("contract", ContractViewset, basename="contract")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
