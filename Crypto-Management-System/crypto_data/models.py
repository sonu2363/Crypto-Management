import uuid
from django.db import models

class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CryptoPrice(models.Model):
    id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='crypto_prices')
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.symbol} - {self.price} USD for {self.org_id.name}"

    class Meta:
        ordering = ['-timestamp']
