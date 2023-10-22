from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("search/", views.PostSearchView.as_view(), name="post_search"),
    path("<slug:post>/", views.single_post, name="single-post"),
    path("tag/<slug:tag>/", views.TagListView.as_view(), name="post-by-tag"),
]
