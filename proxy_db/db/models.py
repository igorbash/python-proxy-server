from django.db import models


class Client(models.Model):
    ip = models.CharField(primary_key=True, max_length=100)


class Cookie(models.Model):
    user_ip = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='cookies')
    cookie = models.CharField(primary_key=True, max_length=2048)


class Credential(models.Model):
    user_ip = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='credentials')
    token = models.CharField(primary_key=True, max_length=1024)
