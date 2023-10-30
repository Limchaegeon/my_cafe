from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('Menus/', views.Menus, name='Menus'),
    path('Menus/details/<int:id>', views.details, name='details'),
]