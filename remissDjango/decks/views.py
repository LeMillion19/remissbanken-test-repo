from rest_framework import viewsets
from rest_framework.response import Response

from .models import Deck
from cards.models import Card
from .serializers import DeckSerializer
from cards.serializers import CardSerializer

# Create your views here.
class DeckViewSet(viewsets.ModelViewSet):
    serializer_class = DeckSerializer
    queryset = Deck.objects.all()
    
class DeckCardsViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    
    def list(self, request, deck_pk):
        cards = Card.objects.filter(deck=deck_pk)
        serializer = self.get_serializer(cards, many=True)
        return Response(serializer.data)