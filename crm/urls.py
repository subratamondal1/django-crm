from django.urls import path

from . import views

urlpatterns: list = [
    path(route="", view=views.home, name="home"),
    # path(route="login/", view=views.login_user, name="login"),
    path(route="logout/", view=views.logout_user, name="logout"),
    path(route="register/", view=views.register_user, name="register"),
    path(route="record/<int:pk>/", view=views.customer_record, name="record"),
    path(
        route="delete_record/<int:pk>/", view=views.delete_record, name="delete_record"
    ),
    path(route="add_record/", view=views.add_record, name="add_record"),
    path(
        route="update_record/<int:pk>", view=views.update_record, name="update_record"
    ),
]
