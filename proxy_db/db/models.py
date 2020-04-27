from django.db import models


class Client(models.Model):
    ip = models.CharField(primary_key=True, max_length=100)


class Cookie(models.Model):
    user_ip = models.ForeignKey(Client, on_delete=models.CASCADE)
    cookie = models.CharField(max_length=100)
    host = models.CharField(max_length=100)


class Credential(models.Model):
    user_ip = models.ForeignKey(Client, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
