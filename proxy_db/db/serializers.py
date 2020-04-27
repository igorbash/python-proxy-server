from .models import Client, Cookie, Credential
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['ip']


class CookieSerializer(serializers.ModelSerializer):
    user_ip = ClientSerializer()

    class Meta:
        model = Cookie
        fields = ['user_ip', 'cookie', 'host']


class CredentialSerializer(serializers.ModelSerializer):
    user_ip = ClientSerializer()

    class Meta:
        model = Credential
        fields = ['user_ip', 'token', 'host']
