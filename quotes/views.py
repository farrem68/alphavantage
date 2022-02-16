from unicodedata import name
from django.shortcuts import render, redirect
from django.conf import settings
#
from django.http import HttpResponse , JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view , permission_classes
from .serializer import AssetPricesModel
#
from .models import asset_prices_model
from .forms import register_form
import requests
import json
import time


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

def prices(request):
    latest_data = asset_prices_model.objects.filter().last()
    context= {"latest_data": latest_data}

    return render(request, 'index.html',context)

def register(request):
    form = register_form(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form":form}
    return render(request, 'register.html',context)


@api_view(['GET',"POST"])
@permission_classes((IsAuthenticated, ))
def quotes(request):
    print(request)
    if request.method == 'GET':
        assets = asset_prices_model.objects.all()
        print(assets)
        serializer = AssetPricesModel(assets,many=True)
        return JsonResponse({"data" : serializer.data},status=201)

    elif request.method == "POST":
        market_stats = get_asset_price("btc","usd",settings.ALPHAVANTAGE_KEY)
        payload= {
            "name":market_stats["coin_name"],
            "code":market_stats['coin_code'],
            "fiat_pair":market_stats["fiat_pair"],
            "price":market_stats["market_value"],
            "best_bid":market_stats["bid_price"],
            "best_ask":market_stats["ask_price"]
        }
        serializer = AssetPricesModel(data = payload)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data" : serializer.data},status=201)
        else:
            return JsonResponse({"data" : serializer.data},status=201)

    else:
        return JsonResponse({"data" : "Invailed Request."}, status=400)


