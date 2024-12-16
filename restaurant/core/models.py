from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    weight = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    dish = models.OneToOneField(
        Dish,
        on_delete=models.CASCADE,
        related_name='recipe'
    )
    time = models.FloatField()  # in minutes
    technology = models.TextField()

    def __str__(self):
        return f"Recipe for {self.dish.name}"


class Cooking(models.Model):
    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
        related_name='cookings'
    )
    amount = models.PositiveIntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return f"Cooking of {self.dish.name} on {self.date}"
