from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ActiveClientForm
from .models import ActiveClient


@login_required
def client_list(request):
    # В шаблоне цикл {% for customer in customers %}
    customers = ActiveClient.objects.all().order_by("-created_at")
    return render(request, "clients/customers-list.html", {"customers": customers})


@login_required
def client_detail(request, pk):
    # В шаблоне {{ object.lead.last_name }}
    obj = get_object_or_404(ActiveClient, pk=pk)
    return render(request, "clients/customers-detail.html", {"object": obj})


@login_required
def client_create(request):
    if request.method == "POST":
        form = ActiveClientForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect("clients:client_detail", pk=obj.pk)
    else:
        form = ActiveClientForm()
    return render(request, "clients/customers-create.html", {"form": form})


@login_required
def client_edit(request, pk):
    obj = get_object_or_404(ActiveClient, pk=pk)
    if request.method == "POST":
        form = ActiveClientForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("clients:client_detail", pk=obj.pk)
    else:
        form = ActiveClientForm(instance=obj)
    return render(request, "clients/customers-edit.html", {"form": form, "object": obj})


@login_required
def client_delete(request, pk):
    obj = get_object_or_404(ActiveClient, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("clients:client_list")
    return render(
        request, "clients/customers-delete.html", {"object": obj, "form": forms.Form()}
    )
