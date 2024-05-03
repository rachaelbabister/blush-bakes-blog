from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Recipe, Comment
from apps.users.models import UserProfile
from .forms import CommentForm


class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def recipe_detail(request, slug):
    """
    Display an individual :model:`blog.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`blog.Recipe`.
    ``comments``
        Approved comments relating to the post.
    ``comment_count``
        The number of approved comments relating to the recipe.
    ``comment_form``
        An instance of :form:`blog.CommentForm`.

    **Template:**

    :template:`blog/recipe_detail.html`
    """

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()
    recipe.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Thank you, your comment will appear once approved."
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/recipe_detail.html",
        {
            "recipe": recipe,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def add_to_favourites(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        user_profile.favourite_recipes.add(recipe)
        messages.success(request, f'Added {recipe.title} to your favourites')
    return redirect('recipe_detail', slug=recipe.slug)


def remove_favourites(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        selected_recipe_ids = request.POST.getlist('selected_recipes')
        if selected_recipe_ids:
            if request.user.is_authenticated:
                user_profile = get_object_or_404(UserProfile, user=request.user)
                user_profile.favourite_recipes.remove(recipe)
                messages.success(request, f'{recipe.title} removed from your favourites')
    return redirect('profile')


def comment_edit(request, slug, comment_id):
    """
    Displays an individual comment for edit.

    **Context**

    ``recipe``
        An instance of :model:`blog.Recipe`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`
    """
    if request.method == "POST":

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Your comment has been updated.")
        else:
            messages.add_message(request, messages.ERROR, "Sorry, there was an error updating your comment")

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Deletes an individual comment.

    **Context**

    ``recipe``
        An instance of :model:`blog.Recipe`.
    ``comment``
        A single comment related to the post.
    """
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comment_query = Comment.objects.all()
    comment = get_object_or_404(comment_query, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Your comment has been deleted.')
    else:
        messages.add_message(request, messages.ERROR, 'Error - you can only delete your own comments.')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))