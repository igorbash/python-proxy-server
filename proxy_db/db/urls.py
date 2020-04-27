from django.urls import path

from .views import ClientListCreateAPIView, ClientDetailsAPIView, CookieListCreateAPIView, CookieDetailsAPIView, \
    CredentialListCreateAPIView, CredentialDetailsAPIView

urlpatterns = [
    path('clients/', ClientListCreateAPIView.as_view(), name='api-client-list'),
    path('clients/<uuid:pk>/', ClientDetailsAPIView.as_view(), name='api-client-details'),
    path('cookies/', CookieListCreateAPIView.as_view(), name='api-cookie-list'),
    path('cookies/<uuid:pk>/', CookieDetailsAPIView.as_view(), name='api-cookie-details'),
    path('credentials/', CredentialListCreateAPIView.as_view(), name='api-credential-list'),
    path('credentials/<uuid:pk>/', CredentialDetailsAPIView.as_view(), name='api-credential-details'),
]
