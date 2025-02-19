from django.forms.widgets import EmailInput
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User
from django import forms
from .forms import RegisterForm

# Create your views here.


def shop_view(request):
    return render(request, "accounts/shop.html", {})


def login_view_1(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
        # return redirect("/admin")
    else:
        form = AuthenticationForm(request)

    context = {"form": form}

    return render(request, "accounts/login.html", context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid username or password."}
            return render(request, "accounts/login.html", context)
        login(request, user)
        return redirect("/")
    return render(request, "accounts/login.html", {})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "accounts/logout.html", {})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect("/login")

    context = {"form": form}
    return render(request, "accounts/register.html", context)


# def register_view_2(request):
#     form = UserCreationForm(request.POST or None)
#     if form.is_valid():
#         user_obj = form.save()
#         return redirect("/login")

#     context = {"form": form}
#     return render(request, "accounts/register.html", context)


# def register_view_1(request):
#     if request.method == "POST":
#         username = request.POST.get("user_name")
#         password = request.POST.get("password")
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")
#         email = request.POST.get("email")

#     form = UserCreationForm(request.POST or None)
#     if form.is_valid():
#         user_obj = form.save()
#         return redirect("/login")

#     context = {"form": form}
#     return render(request, "accounts/register.html", context)


# 3 # # # 3 3
# def login_view(request):

#     if request.method == "POST":
#         form=AuthenticationForm(request,data=request.POST)
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         print(username, password)
#         user = authenticate(request, username=username, password=password)
#         if user is None:
#             context = {"error": "invalid username or password"}
#             return render(request, "accounts/login.html", context)
#         login(request, user)
#         return redirect("/articles/create")
#         # return redirect("/admin")
#     else:
#         form=AuthenticationForm(request)

#     return render(request, "accounts/login.html", {})
