from django.urls import path

from . import views

app_name = "clients"

urlpatterns = [
    path("", views.client_list, name="client_list"),  # /customers/
    path("new/", views.client_create, name="client_create"),  # /customers/new/
    path("<int:pk>/", views.client_detail, name="client_detail"),  # /customers/<id>/
    path(
        "<int:pk>/edit/", views.client_edit, name="client_edit"
    ),  # /customers/<id>/edit/
    path(
        "<int:pk>/delete/", views.client_delete, name="client_delete"
    ),  # /customers/<id>/delete/
]
