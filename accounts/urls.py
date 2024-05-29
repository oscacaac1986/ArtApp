from django.urls import include, path
from rest_framework import routers

from accounts.views import FacebookLogin, GoogleLogin

router = routers.DefaultRouter()
urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login')
]
urlpatterns += router.urls