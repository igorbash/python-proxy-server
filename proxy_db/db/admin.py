from django.contrib import admin

from .models import User, Credential, Cookie

admin.site.register(User)
admin.site.register(Credential)
admin.site.register(Cookie)
