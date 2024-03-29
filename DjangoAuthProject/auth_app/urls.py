from django.urls import path
from .views import *


urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('signup', SignUp.as_view(), name='signup'),
    path('logout', logout, name='logout'),
    path('home', home, name='home'),
    path('profile', profile, name ="profile")
]