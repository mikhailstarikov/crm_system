from django.contrib import admin

from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("name", "service", "amount", "date_signed")
    list_filter = ("service", "date_signed")
