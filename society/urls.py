from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_user, name="login"),
    path("register/", views.register_user, name="register"),
    path("logout/", views.logout_user, name="logout"),
    path("posts/<int:post_id>/likes", views.post_likes, name="post_likes"),
    path("posts/<int:post_id>/likes/<int:like_id>", views.post_likes, name="post_like"),
]