from .models import Client, Cookie, Credential
from rest_framework import serializers


class CookieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookie
        fields = ['user_ip', 'cookie_name', 'cookie', 'host']


class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = ['user_ip', 'token', 'host']


class ClientSerializer(serializers.ModelSerializer):
    cookies = CookieSerializer(many=True, read_only=True)
    credentials = CredentialSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['ip', 'cookies', 'credentials']
