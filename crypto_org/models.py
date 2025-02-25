from django.db import models
import uuid
from decimal import Decimal
from django.contrib.auth.models import AbstractUser

class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CryptoPrice(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.symbol} - {self.price} ({self.timestamp})'

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey('Organization', on_delete=models.SET_NULL, null=True, blank=True)
    
    def is_org_owner(self, org):
        return self.organization == org
    
    def __str__(self):
        return self.username