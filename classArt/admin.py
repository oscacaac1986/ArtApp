from django.contrib import admin
from .models import ArtisticExpressions, TypeArtisticExpression, Level

class ArtisticExpressionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class TypeArtisticExpressionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'art_expression_name')

    def art_expression_name(self, obj):
        return obj.art_expression.name

    art_expression_name.short_description = 'Art Expression'

class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

admin.site.register(ArtisticExpressions, ArtisticExpressionsAdmin)
admin.site.register(TypeArtisticExpression, TypeArtisticExpressionAdmin)
admin.site.register(Level, LevelAdmin)
