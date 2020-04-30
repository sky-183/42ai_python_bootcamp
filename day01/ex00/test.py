# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/29 20:44:04 by vflander          #+#    #+#              #
#    Updated: 2020/04/29 20:44:04 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe

if __name__ == "__main__":
    # testing recipe module here
    test_recipe = Recipe("cake", 3, 60, ["skill", "love"], "dessert", "yum!")
    print(test_recipe)
    wrong_data1 = Recipe("cake1", -1, 60, ["skill", "love"], "dessert", "")
    wrong_data2 = Recipe("cake2", "dw", 60, ["skill", "love"], "dessert", "")
    wrong_data3 = Recipe("cake3", 3, -20, ["skill", "love"], "dessert", "!")
    wrong_data4 = Recipe("cake4", 3, "wd", ["skill", "love"], "dessert", "!")
    wrong_data5 = Recipe("cake5", 3, 60, "not a list", "dessert", "")
    wrong_data6 = Recipe("cake6", 3, 60, ["skill", "love"], "ert", "!")
    wrong_data7 = Recipe("cake7", 3, 60, ["skill", "love"], "", "")
    # testing book module here
    cookbook = Book("Cooking 101")
    print(cookbook)
    cookbook.add_recipe(test_recipe)
    print(cookbook.get_recipes_by_types("as"))
    print(cookbook.get_recipes_by_types("desset"))
    print(cookbook.get_recipe_by_name("caaaake"))
    print(cookbook.get_recipe_by_name("cake"))
