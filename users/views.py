from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render


def user_login(request):
    """Страница входа"""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("services:service_list")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


@login_required
def user_logout(request):
    """Выход из системы"""
    logout(request)
    return redirect("users:login")
