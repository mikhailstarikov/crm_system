from django.urls import path

from . import views

app_name = "services"

urlpatterns = [
    path("", views.service_list, name="service_list"),  # /products/
    path("new/", views.service_create, name="service_create"),  # /products/new/
    path("<int:pk>/", views.service_detail, name="service_detail"),  # /products/<id>/
    path(
        "<int:pk>/edit/", views.service_edit, name="service_edit"
    ),  # /products/<id>/edit/
    path(
        "<int:pk>/delete/", views.service_delete, name="service_delete"
    ),  # /products/<id>/delete/
]
