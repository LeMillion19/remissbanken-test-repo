from django.urls import path, include
from rest_framework_nested import routers

from .views import (
    DeckViewSet, 
    DeckCardsViewSet
)

router = routers.SimpleRouter()
router.register('', DeckViewSet)

# register a '/decks/:id/cards' url here
cards_router = routers.NestedDefaultRouter(router, '', lookup='deck')
cards_router.register('cards', DeckCardsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(cards_router.urls))
]