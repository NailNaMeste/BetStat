from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import BetViewSet, UserViewSet

router = DefaultRouter()
router.register(r'bets', BetViewSet)
router.register(r'user', UserViewSet)

urlpatterns = router.urls
