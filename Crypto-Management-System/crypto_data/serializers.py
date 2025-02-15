from rest_framework import serializers
from .models import Organization, CryptoPrice

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'created_at']

class CryptoPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoPrice
        fields = ['id', 'org_id', 'symbol', 'price', 'timestamp']