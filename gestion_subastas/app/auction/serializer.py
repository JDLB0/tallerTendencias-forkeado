from rest_framework import serializers

from .models import auction

class auctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = auction
        fields = ('__all__')