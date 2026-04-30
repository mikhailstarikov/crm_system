from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ServiceForm
from .models import Service


@login_required
def service_list(request):
    products = Service.objects.filter(is_active=True)
    return render(request, "services/products-list.html", {"products": products})


@login_required
def service_detail(request, pk):
    obj = get_object_or_404(Service, pk=pk)
    return render(request, "services/products-detail.html", {"object": obj})


@login_required
def service_create(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect("services:service_detail", pk=obj.pk)
    else:
        form = ServiceForm()
    return render(request, "services/products-create.html", {"form": form})


@login_required
def service_edit(request, pk):
    obj = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("services:service_detail", pk=obj.pk)
    else:
        form = ServiceForm(instance=obj)
    return render(request, "services/products-edit.html", {"form": form, "object": obj})


@login_required
def service_delete(request, pk):
    obj = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("services:service_list")
    return render(
        request, "services/products-delete.html", {"object": obj, "form": forms.Form()}
    )
