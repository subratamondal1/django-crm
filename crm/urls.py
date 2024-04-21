from django.urls import path

from . import views

urlpatterns: list = [
    path(route="", view=views.home, name="home"),
    # path(route="/login", view=views.login_user, name="login"),
    path(route="/logout", view=views.logout_user, name="logout"),
]
