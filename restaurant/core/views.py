from django.shortcuts import render, get_object_or_404, redirect
from .models import Dish, Recipe, Cooking
from django.utils.timezone import localtime


def index(request):
    return render(request, 'index.html')


# Dish Views
def dish_list(request):
    sort = request.GET.get('sort', 'id')
    order = request.GET.get('order', 'asc')
    dishes = Dish.objects.all()

    if sort in ['id', 'name', 'type', 'weight', 'price']:
        if order == 'desc':
            sort = f'-{sort}'
        dishes = dishes.order_by(sort)
    else:
        return render(request, '404.html')

    return render(request, 'dishes/dish_list.html', {
        'dishes': dishes,
        'current_sort': request.GET.get('sort', 'id'),
        'current_order': request.GET.get('order', 'asc'),
    })


def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'dishes/dish_detail.html', {'dish': dish})


def dish_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        type_ = request.POST['type']
        weight = request.POST['weight']
        price = request.POST['price']

        Dish.objects.create(name=name, type=type_, weight=weight, price=price)
        return redirect('dish_list')

    return render(request, 'dishes/dish_form.html')


def dish_edit(request, pk):
    dish = get_object_or_404(Dish, pk=pk)

    if request.method == 'POST':
        dish.name = request.POST['name']
        dish.type = request.POST['type']
        dish.weight = request.POST['weight']
        dish.price = request.POST['price']
        dish.save()
        return redirect('dish_list')

    return render(request, 'dishes/dish_form.html', {'dish': dish})


def dish_delete(request, pk):
    dish = get_object_or_404(Dish, pk=pk)

    if request.method == 'POST':
        dish.delete()
        return redirect('dish_list')

    return render(request, 'dishes/dish_confirm_delete.html', {'dish': dish})


# Recipe Views
def recipe_list(request):
    sort = request.GET.get('sort', 'id')
    order = request.GET.get('order', 'asc')
    recipes = Recipe.objects.all()

    if sort in ['id', 'dish__name', 'time', 'technology']:
        if order == 'desc':
            sort = f'-{sort}'
        recipes = recipes.order_by(sort)
    else:
        return render(request, '404.html')

    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
        'current_sort': request.GET.get('sort', 'id'),
        'current_order': request.GET.get('order', 'asc'),
    })


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


def recipe_create(request):
    if request.method == 'POST':
        dish_id = request.POST['dish']
        time = request.POST['time']
        technology = request.POST['technology']

        dish = get_object_or_404(Dish, pk=dish_id)
        Recipe.objects.create(dish=dish, time=time, technology=technology)
        return redirect('recipe_list')

    dishes = Dish.objects.all()
    return render(request, 'recipes/recipe_form.html', {'dishes': dishes})


def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == 'POST':
        recipe.dish_id = request.POST['dish']
        recipe.time = request.POST['time']
        recipe.technology = request.POST['technology']
        recipe.save()
        return redirect('recipe_list')

    dishes = Dish.objects.all()
    return render(request, 'recipes/recipe_form.html', {
        'recipe': recipe,
        'dishes': dishes,
    })


def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')

    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})


# Cooking Views
def cooking_list(request):
    sort = request.GET.get('sort', 'id')
    order = request.GET.get('order', 'asc')
    cookings = Cooking.objects.select_related('dish').all()

    if sort in ['id', 'dish__name', 'amount', 'date']:
        if order == 'desc':
            sort = f'-{sort}'
        cookings = cookings.order_by(sort)
    else:
        return render(request, '404.html')

    return render(request, 'cookings/cooking_list.html', {
        'cookings': cookings,
        'current_sort': request.GET.get('sort', 'id'),
        'current_order': request.GET.get('order', 'asc'),
    })


def cooking_detail(request, pk):
    cooking = get_object_or_404(Cooking, pk=pk)
    return render(request, 'cookings/cooking_detail.html', {'cooking': cooking})


def cooking_create(request):
    if request.method == 'POST':
        dish_id = request.POST['dish']
        amount = request.POST['amount']
        date = request.POST['date']

        dish = get_object_or_404(Dish, pk=dish_id)
        Cooking.objects.create(dish=dish, amount=amount, date=date)
        return redirect('cooking_list')

    dishes = Dish.objects.all()
    return render(request, 'cookings/cooking_form.html', {'dishes': dishes})


def cooking_edit(request, pk):
    cooking = get_object_or_404(Cooking, pk=pk)

    if request.method == 'POST':
        cooking.dish_id = request.POST['dish']
        cooking.amount = request.POST['amount']
        cooking.date = request.POST['date']
        cooking.save()
        return redirect('cooking_list')

    # Преобразуем дату в строковый формат
    cooking.date = localtime(cooking.date).strftime('%Y-%m-%dT%H:%M:%S')
    dishes = Dish.objects.all()
    return render(request, 'cookings/cooking_form.html', {
        'cooking': cooking,
        'dishes': dishes,
    })


def cooking_delete(request, pk):
    cooking = get_object_or_404(Cooking, pk=pk)

    if request.method == 'POST':
        cooking.delete()
        return redirect('cooking_list')

    return render(request, 'cookings/cooking_confirm_delete.html', {'cooking': cooking})
