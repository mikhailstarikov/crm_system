from django import forms

from .models import Contract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ["name", "service", "document", "date_signed", "period", "amount"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "service": forms.Select(attrs={"class": "form-control"}),
            "document": forms.FileInput(attrs={"class": "form-control"}),
            "date_signed": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "period": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
        }
