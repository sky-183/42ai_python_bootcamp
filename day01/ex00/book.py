# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/29 20:43:56 by vflander          #+#    #+#              #
#    Updated: 2020/04/29 20:43:56 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
The official documentation for 'book' module
"""

from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name: str):
        """Recipe book
        :param name: str
        """
        self.name = name
        self.recipe_list = dict.fromkeys(["starter", "lunch", "dessert"], [])
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        print(f"Book '{name}' created successfully")

    def __str__(self):
        """Prints the book name"""
        return self.name

    def get_recipe_by_name(self, name: str) -> object:
        """Print a recipe with the given name and return the instance
        :param name: str, recipe name
        :return: instance of Recipe class instance with a given name (or None)
        """
        # searching for a recipe (only the first instance)
        result = None
        for recipe_list in self.recipe_list.values():
            if result is None:
                for recipe in recipe_list:
                    if recipe.name == name:
                        result = recipe
                        break
        # return None here if recipe not found
        if result is None:
            print(f"No recipe named '{name}' found.")
            return
        # found one, printing
        # can move that to recipe.__str__ and just use print here
        print("=" * len(result.name))
        print(result.name)
        print("=" * len(result.name))
        print("Cooking level:", result.cooking_lvl)
        print("Cooking time:", result.cooking_time, "minutes")
        print("Ingredients:", ', '.join(result.ingredients))
        print("Description:", result.description)
        print("Recipe type:", result.recipe_type)
        return result

    def get_recipes_by_types(self, recipe_type: str) -> list:
        """Get all recipe names for a given 'recipe_type'
        :param recipe_type: one of the valid recipe types
        :return: list of names (or empty list on error)
        """
        if not (recipe_type in self.recipe_list.keys()):
            print(f"Recipe type '{recipe_type}' not recognized")
            print(f"Valid recipe types: {', '.join(self.recipe_list.keys())}")
            return []
        names_list = [recipe.name for recipe in self.recipe_list[recipe_type]]
        return names_list

    def add_recipe(self, recipe: Recipe):
        """Add a recipe to the book and update last_update
        :param recipe: Recipe class object
        """
        if not isinstance(recipe, Recipe):
            print(f"{recipe} is not a valid recipe.",
                  "Please, create a valid recipe in official recipe module.")
            return
        self.recipe_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()


if __name__ == "__main__":
    pass
