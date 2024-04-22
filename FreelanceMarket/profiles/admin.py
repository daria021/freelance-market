from django.contrib import admin

from .models import Executor, Client

admin.site.register(Executor)
admin.site.register(Client)
