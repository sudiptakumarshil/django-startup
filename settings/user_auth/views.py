from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    SetPasswordForm,
)
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.http import JsonResponse
from django.views import View
from .services.user_service import UserService
from .repositories.user_repository import UserRepository
import json


class UserRegisterView(View):

    def __init__(self, user_service=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_service = user_service or UserService(repository=UserRepository())

    def get(self, request):
        return render(request, "register.html")

    def post(self, request, id=None):
        data = json.loads(request.body)
        form = RegisterForm(data)
        if form.is_valid():
            result = self.user_service.register_user(form.cleaned_data)
            return JsonResponse(result, safe=False)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("user.profile")
            else:
                messages.warning(request, form.errors.as_text())

        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})
    return redirect("user.profile")


def user_profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html", {"user": request.user})
    return redirect("user.login")


def user_logout(request):
    logout(request)
    return redirect("user.login")


def password_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Password Changed Successfully!!")
                return redirect("user.profile")
            messages.warning(request, form.errors.as_text())
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, "change_password.html", {"form": form})
    return redirect("user.login")


def password_change_except_old(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Password Changed Successfully!!")
                return redirect("user.profile")
            messages.warning(request, form.errors.as_text())
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, "change_password.html", {"form": form})
    return redirect("user.login")


def changeUserProfile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ChangeUserForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "User Info Updated Successfully!!")
                return redirect("user.profile")
            messages.warning(request, form.errors.as_text())
        else:
            form = ChangeUserForm(instance=request.user)
        return render(request, "profile.html", {"form": form})
    return redirect("user.login")
