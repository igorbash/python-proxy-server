from .models import User, Cookie, Credential
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id']


class CookieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cookie
        fields = ['user_id', 'cookie']


class CredentialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Credential
        fields = ['user_id', 'token']
