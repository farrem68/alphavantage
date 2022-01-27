from rest_framework import serializers
from quotes.models import asset_prices_model

class AssetPricesModel(serializers.ModelSerializer):
    class Meta:
        model = asset_prices_model
        fields = [
            "name",
            "code",
            "price",
            "dateTime",
            "fiat_pair",
            "best_bid",
            "best_ask"
        ]