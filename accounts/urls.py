from django.urls import path
from rest_framework import routers

from accounts.views import FacebookLogin, GoogleLogin

router = routers.DefaultRouter()
urlpatterns = [
    path('dj-rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login')
]
urlpatterns += router.urls