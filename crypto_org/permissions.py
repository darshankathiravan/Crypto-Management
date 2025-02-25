from rest_framework import permissions
from .models import Organization, CryptoPrice  # ✅ Add this import

class IsOrgOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.organization:
            return False

        print(f"User Organization ID: {request.user.organization.id}")
        print(f"Object Organization ID: {getattr(obj, 'organization_id', 'None')}") 

        if isinstance(obj, Organization):
            return request.user.organization.id == obj.id

        if isinstance(obj, CryptoPrice):
            return request.user.organization.id == obj.organization.id 

        return False
