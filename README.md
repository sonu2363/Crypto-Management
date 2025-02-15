Crypto Data & Organization Management System
A Django-based system for managing organizations and fetching real-time cryptocurrency prices using the CoinGecko API. The system provides JWT authentication, scheduled price updates via Celery, and complete CRUD operations for both organizations and crypto price data.

Features
Organization Management

Create and manage organizations with unique identifiers
Full CRUD operations with JWT authentication
Organization-specific data isolation
Cryptocurrency Price Tracking

Real-time price data from CoinGecko API
Automatic price updates every 5 minutes
Support for Bitcoin (BTC) and Ethereum (ETH)
Historical price tracking
Authentication & Security

JWT-based authentication
Token refresh mechanism
Permission-based access control
Organization-level data isolation
Technical Stack

Django 4.2.7
Django REST Framework 3.14.0
Celery 5.3.4 for task scheduling
Redis for message broking
SimpleJWT for authentication
CoinGecko API integration
Prerequisites
Python 3.8 or higher
Redis Server
Git (optional)
Installation
Clone the repository (if using Git):
git clone <repository-url>
cd crypto-management
Create and activate virtual environment:
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
Install dependencies:
pip install -r requirements.txt
Install and Configure Redis:

Windows:
Download Redis from: https://github.com/microsoftarchive/redis/releases
Add Redis installation directory to system PATH
Start Redis server: redis-server
Linux/Mac:
sudo apt-get install redis-server  # Ubuntu
brew install redis  # Mac
sudo service redis start  # Ubuntu
brew services start redis  # Mac
Database Setup:

python manage.py migrate  # Create database tables
python manage.py createsuperuser  # Create admin user
Running the Application
Start Django Development Server
python manage.py runserver
Access the application at: http://127.0.0.1:8000/

Start Celery Worker (in a new terminal)
celery -A crypto_management worker --pool=solo -l info  # Windows
celery -A crypto_management worker -l info  # Linux/Mac
Start Celery Beat (in a new terminal)
celery -A crypto_management beat -l info
API Documentation
Authentication Endpoints
Obtain JWT Token
POST /api/token/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}

Response:
{
    "access": "your.access.token",
    "refresh": "your.refresh.token"
}
Refresh Token
POST /api/token/refresh/
Content-Type: application/json

{
    "refresh": "your.refresh.token"
}

Response:
{
    "access": "new.access.token"
}
Organization Endpoints
All organization endpoints require JWT authentication header:

Authorization: Bearer your.access.token
Create Organization
POST /api/organizations/
Content-Type: application/json

{
    "name": "My Organization"
}

Response: 201 Created
{
    "id": "uuid",
    "name": "My Organization",
    "created_at": "2024-02-14T12:00:00Z"
}
List Organizations
GET /api/organizations/

Response: 200 OK
[
    {
        "id": "uuid",
        "name": "My Organization",
        "created_at": "2024-02-14T12:00:00Z"
    }
]
Update Organization
PUT /api/organizations/{uuid}/
Content-Type: application/json

{
    "name": "Updated Organization Name"
}

Response: 200 OK
{
    "id": "uuid",
    "name": "Updated Organization Name",
    "created_at": "2024-02-14T12:00:00Z"
}
Crypto Price Endpoints
Create Price Entry
POST /api/crypto-prices/
Content-Type: application/json

{
    "org_id": "uuid",
    "symbol": "BTC",
    "price": "45000.0000000000"
}

Response: 201 Created
{
    "id": 1,
    "org_id": "uuid",
    "symbol": "BTC",
    "price": "45000.0000000000",
    "timestamp": "2024-02-14T12:00:00Z"
}
Get Latest Prices
GET /api/crypto-prices/latest/?org_id=uuid

Response: 200 OK
[
    {
        "id": 1,
        "org_id": "uuid",
        "symbol": "BTC",
        "price": "45000.0000000000",
        "timestamp": "2024-02-14T12:00:00Z"
    },
    {
        "id": 2,
        "org_id": "uuid",
        "symbol": "ETH",
        "price": "2500.0000000000",
        "timestamp": "2024-02-14T12:00:00Z"
    }
]
Scheduled Tasks
The system automatically fetches cryptocurrency prices every 5 minutes using Celery Beat. The following cryptocurrencies are tracked:

Bitcoin (BTC)
Ethereum (ETH)
Prices are stored for each organization in the system, allowing historical price tracking per organization.

Error Handling
Common HTTP status codes:

200: Successful request
201: Resource created successfully
400: Bad request (invalid data)
401: Unauthorized (invalid/missing token)
403: Forbidden (insufficient permissions)
404: Resource not found
500: Server error
Development
Project Structure
crypto_management/
├── crypto_data/                 # Main application
│   ├── migrations/             # Database migrations
│   ├── models.py              # Data models
│   ├── serializers.py         # API serializers
│   ├── tasks.py              # Celery tasks
│   ├── urls.py               # API routes
│   └── views.py              # API views
├── crypto_management/          # Project settings
│   ├── celery.py             # Celery configuration
│   ├── settings.py           # Django settings
│   └── urls.py               # Main URL routing
├── requirements.txt           # Project dependencies
└── manage.py                 # Django management script
Adding New Features
Create new models in crypto_data/models.py
Create serializers in crypto_data/serializers.py
Add views in crypto_data/views.py
