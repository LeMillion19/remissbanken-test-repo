from django.db import models
from decks.models import Deck

# Create your models here.
class Card(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()
    
    class QuestionTypes(models.IntegerChoices):
        multiple_choice = 1
        fill_in_the_blank = 2
        true_or_false = 3
        short_answer = 4
        
    question_type = models.IntegerField(
        choices= QuestionTypes.choices, default=4)
    
    deck = models.ForeignKey(
        Deck,
        on_delete=models.CASCADE,
        # null=True,
        # blank=True
    )
    
    def __str__(self):
        return self.question