from rest_framework import viewsets

from .models import Deck
from .serializers import DeckSerializer

# Create your views here.
class DeckViewSet(viewsets.ModelViewSet):
    serializer_class = DeckSerializer
    queryset = Deck.objects.all()