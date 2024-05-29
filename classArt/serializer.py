from rest_framework import serializers
from .models import ArtisticExpressions, TypeArtisticExpression, Level

class ArtisticExpressionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtisticExpressions
        fields = '__all__'

class TypeArtisticExpressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeArtisticExpression
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'