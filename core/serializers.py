from rest_framework import serializers
from core.models import Churn
from core.models import Reviews
#Converts high level data to understandable data (JSON, etc)
class ChurnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Churn
        fields = ('ModelPred', 'Review', 'Final')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model= Reviews
        fields=('PlaintextReviews','PosFeedback','NegFeedback','Alt')
