from . import views
from django.urls import path

urlpatterns = [
    path("", views.RecipeList.as_view(), name="home"),
    path("add_to_favourites/<int:recipe_id>/", views.add_to_favourites, name="add_to_favourites"),
    path("remove_favourites/<int:recipe_id>/", views.remove_favourites, name="remove_favourites"),
    path("<slug:slug>/", views.recipe_detail, name="recipe_detail"),
    path("<slug:slug>/edit_comment/<int:comment_id>", views.comment_edit, name="comment_edit"),
    path("<slug:slug>/delete_comment/<int:comment_id>", views.comment_delete, name="comment_delete"),
]