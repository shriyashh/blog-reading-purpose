from django.urls import path,include
from . import views as loginview

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("", loginview.dashboard, name="projectindex"),
    path("register/", loginview.userregister, name="register"),
    path("login/", loginview.userlogin, name="login"),


]