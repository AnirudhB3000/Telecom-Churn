from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
#Database coloumns defined
class Churn(models.Model):
    ModelPred = models.FloatField(max_length=100)
    Review = models.FloatField(max_length=100)
    Final = models.FloatField(max_length=100)

class Reviews(models.Model):
    PlaintextReviews = models.TextField(max_length=500)
    PosFeedback = models.FloatField(max_length=50)
    NegFeedback = models.FloatField(max_length=50)
    Alt = models.FloatField(max_length=100)





