from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request) -> HttpResponse:
    return render(request=request, template_name="home.html", context={})
