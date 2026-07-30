"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    dish_ingredients=set(dish_ingredients)
    return (dish_name,dish_ingredients)

def check_drinks(drink_name, drink_ingredients):
    if set(drink_ingredients) & set(ALCOHOLS):
        return drink_name + " Cocktail"
    else:
        return drink_name + " Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    dish_ingredients = set(dish_ingredients)
    if dish_ingredients <= set(VEGAN):
        return f"{dish_name}: VEGAN"
    elif dish_ingredients <= set(VEGETARIAN):
        return f"{dish_name}: VEGETARIAN"
    elif dish_ingredients <= set(PALEO):
        return f"{dish_name}: PALEO"
    elif dish_ingredients <= set(KETO):
        return f"{dish_name}: KETO"
    else:
        return f"{dish_name}: OMNIVORE"


def tag_special_ingredients(dish):
    dish_name, dish_ingredients = dish         
    special = set(dish_ingredients) & set(SPECIAL_INGREDIENTS)
    return (dish_name, special)