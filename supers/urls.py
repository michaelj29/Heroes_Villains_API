from . import views
from django.urls import path

urlpatterns = [
    path('', views.super_list),
    path('<int:pk>/', views.super_list)
]