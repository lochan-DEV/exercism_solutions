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