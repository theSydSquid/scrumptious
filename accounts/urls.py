from django.urls import path
from accounts.views import signup, user_login, logout_view


urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", user_login, name="user_login"),
    path("logout/", logout_view, name="logout")
]
