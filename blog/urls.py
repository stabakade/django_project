from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),   #emptying the field would mean that since nothing is specified, it is home page
    path('about/', views.about, name="about-path"),
    path('post/new/', PostCreateView.as_view(), name="post_create"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name = "post_update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name = "post_delete"),
    path('post/<int:pk>', PostDetailView.as_view(), name = "post_detail") #we only expect to see integer after post
]   #remember we also have a urls.py in main module, we'll also need to tell which urls.py to follow