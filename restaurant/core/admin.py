from django.contrib import admin
from .models import Dish, Recipe, Cooking


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'weight', 'price')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('dish', 'time', 'technology')


@admin.register(Cooking)
class CookingAdmin(admin.ModelAdmin):
    list_display = ('dish', 'amount', 'date')

