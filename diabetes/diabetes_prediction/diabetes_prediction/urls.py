from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home ),
    path('upload/', views.upload),
    path("predict/", views.predict),
    path("predict/result", views.result),
    path("admin/", admin.site.urls),
]
