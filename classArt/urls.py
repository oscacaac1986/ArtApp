from django.urls import include, path
from rest_framework import routers

from accounts.views import FacebookLogin, GoogleLogin
from classArt.views import ArtisticExpressionsDetail, ArtisticExpressionsList, LevelDetail, LevelList, TypeArtisticExpressionByArtisticExpression, TypeArtisticExpressionDetail, TypeArtisticExpressionList

router = routers.DefaultRouter()
urlpatterns = [
    path('artistic_expressions/', ArtisticExpressionsList.as_view(), name='artistic_expressions_list'),
    path('artistic_expressions/<int:pk>/', ArtisticExpressionsDetail.as_view(), name='artistic_expression_detail'),

    path('type_artistic_expressions/', TypeArtisticExpressionList.as_view(), name='type_artistic_expressions_list'),
    path('type_artistic_expressions/<int:pk>/', TypeArtisticExpressionDetail.as_view(), name='type_artistic_expression_detail'),

    path('levels/', LevelList.as_view(), name='levels_list'),
    path('levels/<int:pk>/', LevelDetail.as_view(), name='level_detail'),
    path('type_artistic_expressions/by_artistic_expression/<int:artistic_expression_id>/', TypeArtisticExpressionByArtisticExpression.as_view(), name='type_artistic_expression_by_artistic_expression'),
]
urlpatterns += router.urls