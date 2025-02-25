# Crypto-Management 🚀

A Django-based system that manages organizations and fetches real-time crypto prices using the CoinGecko API. It features:

- **CRUD APIs** for managing organizations and crypto prices
- **JWT Authentication** for secure access
- **Celery & Redis** for scheduled updates (every 5 minutes)
- **Role-based access control** ensuring restricted data access

# Setup

## Install Dependencies
```sh
pip install -r requirements.txt
```
### Run Celery

```sh
celery -A transket worker --loglevel=info --pool=solo  (worker)

celery -A transket beat --loglevel=info (beat)
```
### Run server

```sh
python manage.py runserver
