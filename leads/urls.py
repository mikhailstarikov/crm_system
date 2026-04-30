from django.urls import path

from . import views

app_name = "leads"

urlpatterns = [
    path("", views.lead_list, name="lead_list"),  # /leads/
    path("new/", views.lead_create, name="lead_create"),  # /leads/new/
    path("<int:pk>/", views.lead_detail, name="lead_detail"),  # /leads/<id>/
    path("<int:pk>/edit/", views.lead_edit, name="lead_edit"),  # /leads/<id>/edit/
    path(
        "<int:pk>/delete/", views.lead_delete, name="lead_delete"
    ),  # /leads/<id>/delete/
]
