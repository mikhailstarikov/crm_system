from django import forms

from .models import AdvertisingCampaign


class AdvertisingCampaignForm(forms.ModelForm):
    class Meta:
        model = AdvertisingCampaign
        fields = ["name", "product", "channel", "budget", "is_active"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "product": forms.Select(attrs={"class": "form-control"}),
            "channel": forms.TextInput(attrs={"class": "form-control"}),
            "budget": forms.NumberInput(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
