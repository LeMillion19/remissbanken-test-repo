from django.db import models
from decks.models import Deck

# Create your models here.
class Card(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()
    
    deck = models.ForeignKey(
        Deck,
        on_delete=models.CASCADE,
        # null=True,
        # blank=True
    )
    
    def __str__(self):
        return self.question