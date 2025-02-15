from django.contrib import admin
from .models import Organization, CryptoPrice

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)

@admin.register(CryptoPrice)
class CryptoPriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'org_id', 'symbol', 'price', 'timestamp')
    list_filter = ('symbol', 'org_id')
    search_fields = ('symbol', 'org_id__name')
