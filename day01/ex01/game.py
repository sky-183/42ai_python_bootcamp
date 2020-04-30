# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/30 08:23:36 by vflander          #+#    #+#              #
#    Updated: 2020/04/30 08:23:36 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class GotCharacter:
    def __init__(self, first_name: str, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Martell(GotCharacter):
    """Its coat of arms is a gold spear piercing a red sun
    on a gold background
    """
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        # family name is equal to class name
        self.family_name = self.__class__.__name__
        self.house_words = "Unbowed, Unbent, Unbroken."

    def die(self):
        self.is_alive = False

    def print_house_words(self):
        print(self.house_words)


if __name__ == "__main__":
    pass
