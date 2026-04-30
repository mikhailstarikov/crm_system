from django.contrib import admin

from .models import ActiveClient


@admin.register(ActiveClient)
class ActiveClientAdmin(admin.ModelAdmin):
    list_display = ("lead", "contract", "created_at")
