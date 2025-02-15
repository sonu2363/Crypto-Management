import requests
from celery import shared_task
from django.conf import settings
from .models import Organization, CryptoPrice

@shared_task
def fetch_crypto_prices():
    # Fetch prices for BTC and ETH
    coins = ['bitcoin', 'ethereum']
    url = f"{settings.COINGECKO_API_URL}/simple/price"
    params = {
        'ids': ','.join(coins),
        'vs_currencies': 'usd'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Get all organizations
        organizations = Organization.objects.all()
        
        # Create price entries for each organization
        for org in organizations:
            # Bitcoin price
            if 'bitcoin' in data:
                CryptoPrice.objects.create(
                    org_id=org,
                    symbol='BTC',
                    price=data['bitcoin']['usd']
                )
            
            # Ethereum price
            if 'ethereum' in data:
                CryptoPrice.objects.create(
                    org_id=org,
                    symbol='ETH',
                    price=data['ethereum']['usd']
                )
                
        return "Prices updated successfully"
    except Exception as e:
        return f"Error fetching prices: {str(e)}"