from django.contrib import admin

from .models import Client, Credential, Cookie

admin.site.register(Client)
admin.site.register(Credential)
admin.site.register(Cookie)
