from django.contrib import admin
from .models import Comanda

class ComandaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comanda,ComandaAdmin)
