from django import forms
from django.contrib.auth.decorators import login_required
from django.db.models import Count, F, Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AdvertisingCampaignForm
from .models import AdvertisingCampaign


@login_required
def ad_list(request):
    ads = AdvertisingCampaign.objects.filter(is_active=True)
    return render(request, "ads/ads-list.html", {"ads": ads})


@login_required
def ad_detail(request, pk):
    obj = get_object_or_404(AdvertisingCampaign, pk=pk)
    return render(request, "ads/ads-detail.html", {"object": obj})


@login_required
def ad_create(request):
    if request.method == "POST":
        form = AdvertisingCampaignForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect("ads:ad_detail", pk=obj.pk)
    else:
        form = AdvertisingCampaignForm()
    return render(request, "ads/ads-create.html", {"form": form})


@login_required
def ad_edit(request, pk):
    obj = get_object_or_404(AdvertisingCampaign, pk=pk)
    if request.method == "POST":
        form = AdvertisingCampaignForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("ads:ad_detail", pk=obj.pk)
    else:
        form = AdvertisingCampaignForm(instance=obj)
    return render(request, "ads/ads-edit.html", {"form": form, "object": obj})


@login_required
def ad_delete(request, pk):
    obj = get_object_or_404(AdvertisingCampaign, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("ads:ad_list")
    return render(request, "ads/ads-delete.html", {"object": obj, "form": forms.Form()})


@login_required
def ad_statistic(request):
    """Статистика по рекламным кампаниям"""
    ads = AdvertisingCampaign.objects.annotate(
        leads_count=Count("leads"),
        customers_count=Count("leads__activeclient"),
        total_revenue=Sum("leads__activeclient__contract__amount"),
    ).annotate(profit=F("total_revenue") - F("budget"))
    return render(request, "ads/ads-statistic.html", {"ads": ads})
