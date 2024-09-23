# users/urls.py

from django.urls import path, include
from users.views import dashboard, register

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),  # No need for regex here
    path("accounts/", include("django.contrib.auth.urls")),  # Same here
    path("register/", register, name="register")
]