from django.contrib import admin
from .models import Abantu

@admin.register(Abantu)
class AbantuAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'address')
    search_fields = ('first_name', 'last_name', 'email')
