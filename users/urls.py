# users/urls.py

from django.urls import path, include
from users.views import register, dashboard

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),  # No need for regex here
    path("accounts/", include("django.contrib.auth.urls")),  # Same here
    path('register/' , register, name='register'),
    path("oauth/", include("social_django.urls"))
]