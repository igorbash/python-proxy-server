from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Client, Cookie, Credential
from db.serializers import CookieSerializer, CredentialSerializer, ClientSerializer


class ClientListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of posts or create new
    """
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete post
    """
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class CookieListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of posts or create new
    """
    serializer_class = CookieSerializer
    queryset = Cookie.objects.all()


class CookieDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete post
    """
    serializer_class = CookieSerializer
    queryset = Cookie.objects.all()


class CredentialListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of posts or create new
    """
    serializer_class = CredentialSerializer
    queryset = Credential.objects.all()


class CredentialDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete post
    """
    serializer_class = CredentialSerializer
    queryset = Credential.objects.all()
