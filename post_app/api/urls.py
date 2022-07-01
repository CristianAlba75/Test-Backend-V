from django.urls import path

from . import views

urlpatterns = [
    path("welcome", views.welcome, name="welcome"),
    path("add_post", views.add_post, name="add_post"),
    path("get_posts/<int:last_id>", views.get_posts, name="get_posts"),
    path("like_post/<int:post_id>", views.like_post, name="like_post"),
    path("dislike_post/<int:post_id>", views.dislike_post, name="dislike_post")
]


