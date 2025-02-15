from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Organization, CryptoPrice
from .serializers import OrganizationSerializer, CryptoPriceSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    """
    API endpoints for Organizations
    
    POST /api/organizations/
    Payload:
    {
        "name": "My Organization"  # Required, unique
    }
    Response: 201 Created
    {
        "id": "uuid",
        "name": "My Organization",
        "created_at": "2024-02-14T12:00:00Z"
    }
    
    GET /api/organizations/
    Response: 200 OK
    [
        {
            "id": "uuid",
            "name": "My Organization",
            "created_at": "2024-02-14T12:00:00Z"
        }
    ]
    
    PUT /api/organizations/{id}/
    Payload:
    {
        "name": "Updated Organization Name"
    }
    Response: 200 OK
    {
        "id": "uuid",
        "name": "Updated Organization Name",
        "created_at": "2024-02-14T12:00:00Z"
    }
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            org = serializer.save()
            return Response(
                self.get_serializer(org).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            org = serializer.save()
            return Response(self.get_serializer(org).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CryptoPriceViewSet(viewsets.ModelViewSet):
    """
    API endpoints for CryptoPrices
    
    POST /api/crypto-prices/
    Payload:
    {
        "org_id": "uuid",  # Required, Organization UUID
        "symbol": "BTC",   # Required, e.g., "BTC" or "ETH"
        "price": "45000.0000000000"  # Required, decimal with up to 10 decimal places
    }
    Response: 201 Created
    {
        "id": 1,
        "org_id": "uuid",
        "symbol": "BTC",
        "price": "45000.0000000000",
        "timestamp": "2024-02-14T12:00:00Z"
    }
    
    GET /api/crypto-prices/?org_id=uuid
    Response: 200 OK
    [
        {
            "id": 1,
            "org_id": "uuid",
            "symbol": "BTC",
            "price": "45000.0000000000",
            "timestamp": "2024-02-14T12:00:00Z"
        }
    ]
    
    GET /api/crypto-prices/latest/?org_id=uuid
    Response: 200 OK
    [
        {
            "id": 1,
            "org_id": "uuid",
            "symbol": "BTC",
            "price": "45000.0000000000",
            "timestamp": "2024-02-14T12:00:00Z"
        }
    ]
    
    PUT /api/crypto-prices/{id}/
    Payload:
    {
        "price": "46000.0000000000"
    }
    Response: 200 OK
    {
        "id": 1,
        "org_id": "uuid",
        "symbol": "BTC",
        "price": "46000.0000000000",
        "timestamp": "2024-02-14T12:00:00Z"
    }
    """
    queryset = CryptoPrice.objects.all()
    serializer_class = CryptoPriceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            price = serializer.save()
            return Response(
                self.get_serializer(price).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = self.queryset
        org_id = self.request.query_params.get('org_id', None)
        if org_id is not None:
            queryset = queryset.filter(id=org_id)
        return queryset

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            price = serializer.save()
            return Response(self.get_serializer(price).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
