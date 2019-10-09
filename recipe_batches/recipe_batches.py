#!/usr/bin/python

import math

# Recipe is a dictionary
# Ingredients is also a dictionary
# Keys are ingredient names, values are amounts (needed for recipe, or available)
def recipe_batches(recipe, ingredients):
    # Declare a holder array of number of batches
    possible_batches = []

    for key in recipe:
        # If we do not have the ingredient, we cannot make the recipe at all. Hence, return 0
        if key not in ingredients:
            return 0

        # If we have more of a particular ingredient than is required in the recipe
        if ingredients[key] // recipe[key] > 0:
            # Divide the amount we have by the amount called for in the recipe
            possible_batches.append(ingredients[key] // recipe[key])
        
        # If we do not have enough of any one ingredient, return 0
        else:
            return 0

    return min(possible_batches) 



if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 60, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))