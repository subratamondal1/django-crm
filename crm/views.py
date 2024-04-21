from django.shortcuts import (
    render,
    redirect,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignUpForm
from .models import Record


# Create your views here.


# The Login is implemented in the 'home' view itself
def home(
    request,
) -> HttpResponse | HttpResponsePermanentRedirect | HttpResponseRedirect:
    # Fetch and store all the records
    records = Record.objects.all()

    if request.method == "POST":  # logging in the user
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate
        user = authenticate(request=request, username=username, password=password)
        if user:
            login(request=request, user=user)
            messages.success(request=request, message="✅ You have been logged in!!!")
            return redirect(to="home")
        else:
            messages.error(
                request=request,
                message="❌ Invalid Credentials. Please provide correct details.",
            )
            return redirect(to="home")
    else:  # this part executes only if the user is already logged in
        return render(
            request=request, template_name="home.html", context={"records": records}
        )


# def login_user(request):
#     pass


def logout_user(request) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    logout(request=request)
    messages.success(request=request, message="✅ You have been logged out.")
    return redirect(to="home")


def register_user(
    request,
) -> HttpResponse | HttpResponseRedirect | HttpResponsePermanentRedirect:
    # If the user is filling up the form and sending post request to register
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and Login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request=request, username=username, password=password)
            login(request=request, user=user)
            messages.success(
                request=request,
                message="✅ You have been successfully registered. Welcome!",
            )
            return redirect(to="home")
    else:
        form = SignUpForm()
        return render(
            request=request, template_name="register.html", context={"form": form}
        )
    return render(
        request=request, template_name="register.html", context={"form": form}
    )
