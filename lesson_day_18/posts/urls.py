from django.urls import path
from .views import HomePageView, ActorPageView, CategoryPageView, CountryPageView, LanguagePageView

urlpatterns = [
    path("", HomePageView.as_view(), name = "home"),
    path("actor/", ActorPageView.as_view(), name = "actor"),
    path("category/", CategoryPageView.as_view(), name = "category"),
    path("country/", CountryPageView.as_view(), name = "country"),
    path("language/", LanguagePageView.as_view(), name = "language"),
]
