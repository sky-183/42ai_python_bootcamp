# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/29 20:44:14 by vflander          #+#    #+#              #
#    Updated: 2020/04/29 20:44:14 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
The official documentation for 'recipe' module
"""


class Recipe:
    def __init__(self, name: str, cooking_lvl: int, cooking_time: int,
                 ingredients: list, recipe_type: str, description=""):
        """
        :param name: str
        :param cooking_lvl: int, range 1 to 5 (included)
        :param cooking_time: int, in minutes (no negative numbers)
        :param ingredients: list of strings
        :param description: str
        :param recipe_type: str, can be "starter", "lunch" or "dessert"
        """
        # TODO:
        # check all values before creating object
        recipe_types_set = {"starter", "lunch", "dessert"}
        try:
            if not (1 <= int(cooking_lvl) <= 5):
                print(f"Wrong 'cooking_lvl' value ({int(cooking_lvl)}),",
                      "should be between 1 and 5")
                return
        except (ValueError, TypeError):
            print("'cooking_lvl' needs to be a number")
            return
        try:
            if int(cooking_time) <= 0:
                print(f"Wrong 'cooking_time' value ({int(cooking_time)}),",
                      "should be positive")
                return
        except (ValueError, TypeError):
            print("'cooking_time' must be a number")
            return
        if not (recipe_type in recipe_types_set):
            print(f"Unknown 'recipe_type' ({recipe_type})")
            print("Valid types are:", *recipe_types_set)
            return
        if not isinstance(ingredients, list):
            print("'ingredients' should be a list")
            return
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        print(f"Recipe '{name}' created successfully.")

    def __str__(self):
        """Printable representation of class instance"""
        txt = f"Recipe '{self.name}'"
        if self.description:
            txt += f" ({self.description})"
        return txt


if __name__ == "__main__":
    pass
