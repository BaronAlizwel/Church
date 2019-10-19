from django.urls import path

from .views import _login, login_user, _logout, signup, signup_user, user_profile


urlpatterns = [
    # Login URLConfs
    path("login/", login_user, name="login_user"),
    path("_login_/", _login, name="_login"),
    path('logout/', _logout, name="_logout"),
    path('profile/', user_profile, name="user_profile"),

    # Signup URLConfs
    path("signup/", signup, name="signup"),
    path("signup_user/", signup_user, name="signup_user"),
]