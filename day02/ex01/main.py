# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/02 18:47:34 by vflander          #+#    #+#              #
#    Updated: 2020/05/02 18:47:34 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


def what_are_the_vars(*args, **kwargs) -> object:
    """returns the object with the right attributes
    :param args:    unnamed args
    :param kwargs:  keyword (named) args
    :return:        object
    """
    obj = ObjectC()
    for i in range(len(args)):
        setattr(obj, f"var_{i}", args[i])
    for key, value in kwargs.items():
        # looks like example prefer errors and not just changing var number
        if hasattr(obj, key):
            return None
        setattr(obj, key, value)
    return obj


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
