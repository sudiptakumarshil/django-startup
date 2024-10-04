from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangeUserForm
from django.contrib import messages
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    SetPasswordForm,
)
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from .repositories.user_register_repository import UserRegisterRepository
from django.http import HttpResponse


def user_register(request):
    user_repository = UserRegisterRepository()
    data = {"name": "Sudipto", "age": 23}
    return HttpResponse(
        user_repository.registerUser(data), content_type="application/json"
    )

    # if not request.user.is_authenticated:
    #     if request.method == "POST":
    #         form = RegisterForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             messages.success(request, "User created Successfully!!")
    #             print(form.cleaned_data)
    #         else:
    #             messages.warning(request, form.errors.as_text())
    #             print(form.errors)
    #     form = RegisterForm()
    #     return render(request, "register.html", {"form": form})
    # return redirect("user.profile")


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
