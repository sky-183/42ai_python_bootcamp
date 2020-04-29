# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/29 13:05:04 by vflander          #+#    #+#              #
#    Updated: 2020/04/29 13:05:04 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}


def print_recipe(recipe_name: str):
    """Prints the recipe from the cookbook
    :param recipe_name:
    """
    print("=" * len(recipe_name))
    print(recipe_name)
    print("=" * len(recipe_name))
    for key, value in cookbook[recipe_name].items():
        if key == "prep_time":
            print("preparation time: ", end="")
        else:
            print(key + ": ", end="")
        if key == "ingredients":
            print(", ".join(value))
        elif key == "prep_time":
            print(value, "minutes")
        else:
            print(value)
    print()


def print_all_recipes(cook_book: dict):
    """Prints all the recipes from the cookbook
    :param cook_book:
    """
    for recipe in cook_book:
        print_recipe(recipe)


def delete_recipe(recipe_name: str):
    """Deletes the recipe from the cookbook
    :param recipe_name: str
    """
    try:
        del cookbook[recipe_name]
        print(f"Recipe for \"{recipe_name}\" removed from the cookbook.")
    except KeyError:
        print(f"No recipe with name \"{recipe_name}\" found :-/")


def add_recipe(recipe_name: str, ingredients: list, meal: str, prep_time: int):
    """Adds a new recipe to the cookbook
    :param recipe_name: str
    :param ingredients: list of str
    :param meal: str
    :param prep_time: int (minutes)
    """
    cookbook[recipe_name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }
    print(f"Recipe for \"{recipe_name}\" added successfully")


def runner():
    """Runs the main program and interacts with the user
    """
    menu = (
        "Please select an option by typing the corresponding number:\n"
        "1: Add a recipe\n"
        "2: Delete a recipe\n"
        "3: Print a recipe\n"
        "4: Print the cookbook\n"
        "5: Quit\n"
    )
    wrong_input = (
        "This option does not exist, please type the corresponding number.\n"
        "To exit, enter 5.\n"
    )
    while True:
        print(menu)
        user_input = input()
        # keep asking for input until 1-5 is entered
        while user_input not in set(map(str, range(1, 6))):
            print(menu)
            print(wrong_input)
            user_input = input()
        # choosing menu options
        if user_input == "1":
            add_name = input("Recipe name:\n")
            add_ing = input("Ingredients list (separated by , )\n").split(",")
            add_meal = input("Meal type:\n")
            time_is_ok = False
            while not time_is_ok:
                try:
                    # floats are also okay here
                    add_time = int(input("Preparation time (in minutes):\n"))
                    time_is_ok = True
                except ValueError:
                    print("That doesnt look like a minutes. Let's try again\n")
            add_recipe(add_name, add_ing, add_meal, add_time)
        elif user_input == "2":
            print("Current recipes:", ', '.join(cookbook.keys()))
            recipe_name = input("Delete which recipe?\n")
            delete_recipe(recipe_name)
        elif user_input == "3":
            print("Current recipes:", ', '.join(cookbook.keys()))
            recipe_name = input("Print what recipe?\n")
            print_recipe(recipe_name)
        elif user_input == "4":
            print_all_recipes(cookbook)
        elif user_input == "5":
            print("Cookbook closed.")
            break
        else:
            # for debug purposes
            print("you should not be here, traveller!")


if __name__ == "__main__":
    runner()
