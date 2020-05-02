# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/02 18:11:01 by vflander          #+#    #+#              #
#    Updated: 2020/05/02 18:11:01 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_reduce(function_to_apply, list_of_inputs):
    """Accumulates the result of function (taking 2 arguments) in the left
    value, reducing the list with each iteration
    :param function_to_apply:   function, taking 2 arguments
    :param list_of_inputs:      iterable
    :return:                    single item
    """
    my_list = list_of_inputs
    if len(my_list) == 0:
        return None
    while len(my_list) > 1:
        my_list[0] = function_to_apply(my_list[0], my_list.pop(1))
    return my_list[0]


def mult(a, b):
    """return a * b
    :param a:   int/float
    :param b:   int/float
    :return:    int/float
    """
    return a * b


if __name__ == "__main__":
    test_list = list(range(1, 6))
    print(ft_reduce(mult, test_list))
