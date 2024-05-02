from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile.as_view(), name="profile"),
    path("", views.signup.as_view(), name="signup"),
]