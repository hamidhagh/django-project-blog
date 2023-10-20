from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("<slug:post>/", views.single_post, name="single-post"),
]
