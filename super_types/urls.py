from . import views
from django.urls import path

urlpatterns = [
    path('', views.super_types_list),
    path('<int:fk>/', views.super_types_detail)
]