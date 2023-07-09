from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import ValidationError


from society.forms import LoginForm, RegisterForm

# @login_required
def index(request):
    return render(request, "index.html")


def logout_user(request):
    if request.method == "GET": 
        logout(request)
        return redirect("/")

def login_user(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    if request.method == "POST":
        form = LoginForm(
            data=request.POST  # ANNOYING AF. INCONSISTENCY -> https://stackoverflow.com/questions/8421200/using-authenticationform-in-django
        )
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                form.add_error("password", ValidationError("user doesn't exist"))               
        return render(request, "login.html", {"form": form})


def register_user(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "register.html", {"form": form})
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password1"],
            )
            login(request, user)
            return redirect("/")
        return render(request, "register.html", {"form": form})
