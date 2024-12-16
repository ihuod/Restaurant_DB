from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    # Dish URLs
    path('dishes/', views.dish_list, name='dish_list'),
    path('dishes/<int:pk>/', views.dish_detail, name='dish_detail'),
    path('dishes/create/', views.dish_create, name='dish_create'),
    path('dishes/<int:pk>/edit/', views.dish_edit, name='dish_edit'),
    path('dishes/<int:pk>/delete/', views.dish_delete, name='dish_delete'),

    # Recipe URLs
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/create/', views.recipe_create, name='recipe_create'),
    path('recipes/<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),
    path('recipes/<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),

    # Cooking URLs
    path('cookings/', views.cooking_list, name='cooking_list'),
    path('cookings/<int:pk>/', views.cooking_detail, name='cooking_detail'),
    path('cookings/create/', views.cooking_create, name='cooking_create'),
    path('cookings/<int:pk>/edit/', views.cooking_edit, name='cooking_edit'),
    path('cookings/<int:pk>/delete/', views.cooking_delete, name='cooking_delete'),
]
