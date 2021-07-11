from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Bet, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('login', 'password', 'bank')


class BetSerializer(ModelSerializer):
    class Meta:
        model = Bet
        fields = '__all__'
    



