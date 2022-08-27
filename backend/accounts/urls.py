from django.urls import path
from django.contrib.auth.views import LoginView

from .views import SignupPageView


urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path("signup/", SignupPageView.as_view(), name="signup"),
]


