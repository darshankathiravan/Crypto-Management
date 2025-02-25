# crypto_org/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizationViewSet, CryptoPriceViewSet

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'crypto-prices', CryptoPriceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
