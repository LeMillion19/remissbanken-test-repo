from django.db import router
from rest_framework import routers, urlpatterns
from .views import CardViewSet

router = routers.SimpleRouter()
router.register('', CardViewSet)

urlpatterns = router.urls