from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/<str:category_name>/', views.post_list, name='post_list'),
]
