from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Organization, CryptoPrice
from .serializers import OrganizationSerializer, CryptoPriceSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOrgOwner 

# Organization Views (CRUD)
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated, IsOrgOwner]

# Crypto Price Views (CRUD)
class CryptoPriceViewSet(viewsets.ModelViewSet):
    queryset = CryptoPrice.objects.all()
    serializer_class = CryptoPriceSerializer
    permission_classes = [IsAuthenticated, IsOrgOwner]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, "organization") and user.organization:
            return CryptoPrice.objects.filter(organization=user.organization)
        return CryptoPrice.objects.none()

