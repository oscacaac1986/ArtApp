from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from ArtApp.permissions import IsAdminOrReadOnly
from .models import ArtisticExpressions, TypeArtisticExpression, Level
from .serializer import ArtisticExpressionsSerializer, TypeArtisticExpressionSerializer, LevelSerializer

class ArtisticExpressionsList(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return ArtisticExpressions.objects.all()

    def get(self, request, format=None):
        artistic_expressions = self.get_queryset()
        serializer = ArtisticExpressionsSerializer(artistic_expressions, many=True)
        return Response(serializer.data)

class ArtisticExpressionsDetail(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return ArtisticExpressions.objects.all()

    def get(self, request, pk, format=None):
        artistic_expression = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = ArtisticExpressionsSerializer(artistic_expression)
        return Response(serializer.data)

class TypeArtisticExpressionList(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return TypeArtisticExpression.objects.all()

    def get(self, request, format=None):
        type_artistic_expressions = self.get_queryset()
        serializer = TypeArtisticExpressionSerializer(type_artistic_expressions, many=True)
        return Response(serializer.data)

class TypeArtisticExpressionDetail(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return TypeArtisticExpression.objects.all()

    def get(self, request, pk, format=None):
        type_artistic_expression = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = TypeArtisticExpressionSerializer(type_artistic_expression)
        return Response(serializer.data)

class LevelList(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Level.objects.all()

    def get(self, request, format=None):
        levels = self.get_queryset()
        serializer = LevelSerializer(levels, many=True)
        return Response(serializer.data)

class LevelDetail(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Level.objects.all()

    def get(self, request, pk, format=None):
        level = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = LevelSerializer(level)
        return Response(serializer.data)

class TypeArtisticExpressionByArtisticExpression(APIView):
    
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return TypeArtisticExpression.objects.all()

    def get(self, request, artistic_expression_id, format=None):
        type_artistic_expressions = self.get_queryset().filter(art_expression_id=artistic_expression_id)
        serializer = TypeArtisticExpressionSerializer(type_artistic_expressions, many=True)
        return Response(serializer.data)
