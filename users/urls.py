from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("", views.user_login, name="login"),
    path("accounts/login/", views.user_login, name="login"),
    path("accounts/logout/", views.user_logout, name="logout"),
]
