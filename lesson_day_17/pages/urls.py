from django.urls import path
from .views import AboutPageView, HomePageView, InfoPageView, LoginPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("info/", InfoPageView.as_view(), name="info"),
    path("login/", LoginPageView.as_view(), name="login"),
]
