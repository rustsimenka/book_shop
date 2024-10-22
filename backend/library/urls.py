from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('library/', views.index_library),
    path('cats/', views.categories),
    path('library/', views.index_library),
    ]