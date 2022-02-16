from __future__ import absolute_import, unicode_literals
from core.celery import app
from .models import asset_prices_model
import requests
import json
from django.conf import settings

def get_asset_price(asset,currency,apikey):
    url = 'https://www.alphavantage.co/query?'
    data = {
        'function':'CURRENCY_EXCHANGE_RATE',
        'from_currency':asset.upper(),
        'to_currency':currency.upper(),
        'apikey':apikey
    }
    priceData = json.loads(requests.get(url,data).text)
    response = {}
    data = priceData['Realtime Currency Exchange Rate']
    response["coin_code"]       = data['1. From_Currency Code']
    response["coin_name"]       = data['2. From_Currency Name']
    response["fiat_pair"]       = data['3. To_Currency Code']
    response["market_value"]    = data['5. Exchange Rate']
    response["bid_price"]       = data['8. Bid Price']
    response["ask_price"]       = data['9. Ask Price']
    
    return response

@app.task(bind=True,name="update_price_table")
def update_price_table(self):
    market_stats = get_asset_price("btc","usd",settings.ALPHAVANTAGE_KEY)
    return asset_prices_model.objects.create(name=market_stats["coin_name"],code=market_stats['coin_code'],fiat_pair=market_stats["fiat_pair"],price=market_stats["market_value"],best_bid=market_stats["bid_price"],best_ask=market_stats["ask_price"])


app.conf.beat_schedule = {
    'Update_pricing_table': {
        'task': 'update_price_table',  
        'schedule': 60.0,
        # 'schedule': 3600.0,
    }
}