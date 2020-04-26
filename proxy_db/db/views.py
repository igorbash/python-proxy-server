from .models import User, Cookie, Credential
from rest_framework import viewsets
from rest_framework import permissions
from db.serializers import UserSerializer, CookieSerializer, CredentialSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class CookieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Cookie.objects.all()
    serializer_class = CookieSerializer
    permission_classes = [permissions.IsAuthenticated]


class CredentialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer
    permission_classes = [permissions.IsAuthenticated]
