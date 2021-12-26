from django.db import router
from rest_framework import routers, urlpatterns
from .views import DeckViewSet

router = routers.SimpleRouter()
router.register('', DeckViewSet)

urlpatterns = router.urls