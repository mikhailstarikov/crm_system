from django.urls import path

from . import views

app_name = "ads"

urlpatterns = [
    path("", views.ad_list, name="ad_list"),  # /ads/
    path("new/", views.ad_create, name="ad_create"),  # /ads/new/
    path("statistic/", views.ad_statistic, name="ad_statistic"),  # /ads/statistic/
    path("<int:pk>/", views.ad_detail, name="ad_detail"),  # /ads/<id>/
    path("<int:pk>/edit/", views.ad_edit, name="ad_edit"),  # /ads/<id>/edit/
    path("<int:pk>/delete/", views.ad_delete, name="ad_delete"),  # /ads/<id>/delete/
]
