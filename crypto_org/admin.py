from django.contrib import admin

# Register your models here.
from .models import Organization, CryptoPrice
from django.contrib.auth import get_user_model

admin.site.register(Organization)
admin.site.register(CryptoPrice)

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'organization']  
    list_filter = ['organization']  