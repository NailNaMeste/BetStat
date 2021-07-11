from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Bet, User
from .serializers import BetSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class BetViewSet(viewsets.ModelViewSet):
    serializer_class = BetSerializer
    queryset = Bet.objects.all()




