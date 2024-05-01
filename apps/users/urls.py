from django.urls import path
from profiles import views

urlpatterns = [
    path('users/', views.profile, name='profile'),
    path('users/', views.signup, name='signup'),
]
