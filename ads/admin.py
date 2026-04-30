from django.contrib import admin

from .models import AdvertisingCampaign


@admin.register(AdvertisingCampaign)
class AdvertisingCampaignAdmin(admin.ModelAdmin):
    list_display = ("name", "product", "budget", "channel", "is_active")
    list_filter = ("product", "is_active")
