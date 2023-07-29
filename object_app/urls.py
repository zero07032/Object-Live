from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("addblog/", views.AddBlog, name="addblog"),
    path("BlogApdateView/<int:pk>/", views.BlogApdateView, name="BlogApdateView"),
    path("UpdateBlog/<int:pk>/", views.UpdateBlog, name="UpdateBlog"),
]

urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]
