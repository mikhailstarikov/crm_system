from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LeadForm
from .models import Lead


@login_required
def lead_list(request):
    leads = Lead.objects.all().order_by("-created_at")
    return render(request, "leads/leads-list.html", {"leads": leads})


@login_required
def lead_detail(request, pk):
    obj = get_object_or_404(Lead, pk=pk)
    return render(request, "leads/leads-detail.html", {"object": obj})


@login_required
def lead_create(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect("leads:lead_detail", pk=obj.pk)
    else:
        form = LeadForm()
    return render(request, "leads/leads-create.html", {"form": form})


@login_required
def lead_edit(request, pk):
    obj = get_object_or_404(Lead, pk=pk)
    if request.method == "POST":
        form = LeadForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("leads:lead_detail", pk=obj.pk)
    else:
        form = LeadForm(instance=obj)
    return render(request, "leads/leads-edit.html", {"form": form, "object": obj})


@login_required
def lead_delete(request, pk):
    obj = get_object_or_404(Lead, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("leads:lead_list")
    return render(
        request, "leads/leads-delete.html", {"object": obj, "form": forms.Form()}
    )
