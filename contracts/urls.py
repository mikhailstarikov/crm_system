from django.urls import path

from . import views

app_name = "contracts"

urlpatterns = [
    path("", views.contract_list, name="contract_list"),  # /contracts/
    path("new/", views.contract_create, name="contract_create"),  # /contracts/new/
    path(
        "<int:pk>/", views.contract_detail, name="contract_detail"
    ),  # /contracts/<id>/
    path(
        "<int:pk>/edit/", views.contract_edit, name="contract_edit"
    ),  # /contracts/<id>/edit/
    path(
        "<int:pk>/delete/", views.contract_delete, name="contract_delete"
    ),  # /contracts/<id>/delete/
]
