"""Functions to manage a users shopping cart items."""

def add_item(current_cart, items_to_add):
    for items in items_to_add:
        if items in current_cart:
            current_cart[items]=current_cart[items]+1
        else:
            current_cart[items]=1
    return current_cart

def read_notes(notes):
    newdict=dict.fromkeys(notes, 1)
    return newdict

def update_recipes(ideas, recipe_updates):
    x=ideas.update(recipe_updates)
    return ideas

def sort_entries(cart):
    sorted_cart=dict(sorted(cart.items()))
    return sorted_cart
