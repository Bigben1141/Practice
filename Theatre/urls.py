from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', Actors.as_view(), name='home'),
    path('actors/', Actor.as_view(), name='actors'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Auth.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
