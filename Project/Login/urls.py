from django.urls import path
from . import views

app_name='Login'
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("main_login/", views.MainLoginView.as_view(), name='main_login'),
]