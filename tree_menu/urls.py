from django.urls import path
from tree_menu import views


urlpatterns = [
    path("", views.index),
    path("<path:cat_slug>/", views.index, name='menu'),
]
