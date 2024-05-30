from django.db import models

# Create your models here.

class ArtisticExpressions(models.Model):
    name= models.CharField(max_length=255, blank=False, null=False)

class TypeArtisticExpression(models.Model):
    name= models.CharField(max_length=255, blank=False, null=False)
    art_expression = models.ForeignKey(ArtisticExpressions, on_delete=models.CASCADE)

class Level(models.Model):
    name= models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)






