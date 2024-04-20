from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    # Check if the user is logging in i.e sending POST Request
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate
        user = authenticate(request=request, username=username, password=password)
        if user:
            login(request=request, user=user)
            messages.success(request=request, message="✅ You have been logged in!!!")
            return redirect(to="home")
        else:
            messages.error(request=request, message="❌ Invalid Credentials. Please provide correct details.")
            return redirect(to="home")
    else:
        # If not logging in means already an user, send them to home
        return render(request=request, template_name="home.html", context={})

# def login_user(request):
#     pass

# def logout_user(request):
#     pass