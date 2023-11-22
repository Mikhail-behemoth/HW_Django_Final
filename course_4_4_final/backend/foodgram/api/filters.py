from django_filters import rest_framework as filters

from recipes.models import Ingredient, Recipe
from users.models import User


class IngredientFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='startswith')

    class Meta:
        model = Ingredient
        fields = ('name',)


class RecipeFilter(filters.FilterSet):
    author = filters.ModelChoiceFilter(queryset=User.objects.all())
    tags = filters.AllValuesMultipleFilter(field_name='tags__slug')
    is_in_shopping_cart = filters.BooleanFilter(
        method='get_is_in_shopping_cart')
    is_favorited = filters.BooleanFilter(method='get_is_favorited')

    def get_is_favorited(self, queryset, name, value):
        if self.request.user.is_authenticated and value:
            return queryset.filter(favorites__user=self.request.user)
        return queryset

    def get_is_in_shopping_cart(self, queryset, name, value):
        if self.request.user.is_authenticated and value:
            return Recipe.objects.filter(
                shopping_cart__user=self.request.user)
        return Recipe.objects.all()

    class Meta:
        model = Recipe
        fields = ('author', 'tags')
