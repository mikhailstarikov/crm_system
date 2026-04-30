from django import forms

from .models import ActiveClient


class ActiveClientForm(forms.ModelForm):
    class Meta:
        model = ActiveClient
        fields = ["lead", "contract"]  # Пользователь выбирает Лида и Контракт
        widgets = {
            "lead": forms.Select(attrs={"class": "form-control"}),
            "contract": forms.Select(attrs={"class": "form-control"}),
        }
