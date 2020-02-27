# accounts/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('homeGet/', views.homeGet, name='homeGet'),
]