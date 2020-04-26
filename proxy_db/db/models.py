from django.db import models


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=100)


class Cookie(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cookie = models.BinaryField()


class Credential(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.BinaryField()
