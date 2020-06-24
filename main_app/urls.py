from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create/', views.WishCreate.as_view(), name='wish_create_form'),
    path('create/wish/', views.wish_create, name='wish_create'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
               