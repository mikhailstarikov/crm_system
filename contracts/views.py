from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContractForm
from .models import Contract


@login_required
def contract_list(request):
    contracts = Contract.objects.all().order_by("-created_at")
    return render(request, "contracts/contracts-list.html", {"contracts": contracts})


@login_required
def contract_detail(request, pk):
    obj = get_object_or_404(Contract, pk=pk)
    return render(request, "contracts/contracts-detail.html", {"object": obj})


@login_required
def contract_create(request):
    if request.method == "POST":
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return redirect("contracts:contract_detail", pk=obj.pk)
    else:
        form = ContractForm()
    return render(request, "contracts/contracts-create.html", {"form": form})


@login_required
def contract_edit(request, pk):
    obj = get_object_or_404(Contract, pk=pk)
    if request.method == "POST":
        form = ContractForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("contracts:contract_detail", pk=obj.pk)
    else:
        form = ContractForm(instance=obj)
    return render(
        request, "contracts/contracts-edit.html", {"form": form, "object": obj}
    )


@login_required
def contract_delete(request, pk):
    obj = get_object_or_404(Contract, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("contracts:contract_list")
    return render(
        request,
        "contracts/contracts-delete.html",
        {"object": obj, "form": forms.Form()},
    )
