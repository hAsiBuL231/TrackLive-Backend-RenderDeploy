from django.urls import path, include

from authentication.View_register import RegistrationView
from authentication.View_login import LoginView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("register", RegistrationView.as_view()),
    path("register/<int:pk>", RegistrationView.as_view()),
    # path("login", obtain_auth_token)
    path("login", LoginView.as_view())
]

