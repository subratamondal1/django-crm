from django.shortcuts import (
    render,
    redirect,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignUpForm, AddRecordForm
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


def customer_record(
    request, pk
) -> HttpResponse | HttpResponseRedirect | HttpResponsePermanentRedirect:
    if request.user.is_authenticated:
        # Look up the Record
        record = Record.objects.get(id=pk)
        return render(
            request=request,
            template_name="record.html",
            context={"customer_record": record},
        )
    else:
        messages.success(
            request=request,
            message="⚠️ You must be logged in to view this page!",
        )
        return redirect(to="home")


def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(
            request=request,
            message="⚠️ Record deleted successfully!",
        )
        return redirect(to="home")
    else:
        messages.success(
            request=request,
            message="⚠️ You must be logged in to perform this operation!",
        )
        return redirect(to="home")

def add_record(request):
    form = AddRecordForm(data=request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request=request, message="✅ Record Added Successfully.")
                return redirect(to="home")
        # If not POSTing
        return render(request=request, template_name="add_record.html", context={"form":form})
    else:
        messages.success(
            request=request,
            message="⚠️ You must be logged in...",
        )
        return redirect(to="home")
    