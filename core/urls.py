from django.urls import path
from .views import HomePageView, GroupsView


app_name = "core"


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("groups/", GroupsView.as_view(), name="groups"),
]