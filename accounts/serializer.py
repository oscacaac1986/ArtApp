from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):

    GENDER = [
        ('M', 'Male'),
        ('F','Female')
    ]
    first_name = serializers.CharField(max=255,required= True)
    secont_name =  serializers.CharField(max=255,required= False)
    first_last_name = serializers.CharField(max=255, required= True)
    secont_last_name =serializers.CharField(max=255, required= False)
    phone_number = serializers.CharField(required=True)
    gender = serializers.ChoiceField(choices=GENDER, default= 'M')
    email = serializers.EmailField(required=True)
    address = serializers.CharField(required=True)