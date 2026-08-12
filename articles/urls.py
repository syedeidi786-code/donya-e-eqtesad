from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home",
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard",
    ),

    path(
        "create/",
        views.article_create,
        name="article_create",
    ),

    path(
        "article/<int:id>/",
        views.article_detail,
        name="article_detail",
    ),

    path(
        "article/<int:id>/edit/",
        views.article_update,
        name="article_update",
    ),

    path(
        "article/<int:id>/delete/",
        views.article_delete,
        name="article_delete",
    ),

  path(
    "article/<int:id>/like/",
    views.like_article,
    name="like_article",
),

path(
    "article/<int:id>/comment/",
    views.add_comment,
    name="add_comment",
),

]