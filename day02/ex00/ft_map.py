# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/02 18:10:41 by vflander          #+#    #+#              #
#    Updated: 2020/05/02 18:10:41 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_map(function_to_apply, list_of_inputs):
    """Applies given function to each element in the list,
    yielding the result values
    :param function_to_apply:   function
    :param list_of_inputs:      iterable
    :return:                    list of results
    """
    # not implementing here taking multiple iterators here. yet.
    for item in list_of_inputs:
        yield function_to_apply(item)


def square(x: int) -> int:
    """Return x**2
    :param x:   int
    :return:    int
    """
    return x * x


if __name__ == "__main__":
    test_list = list(range(10))
    print(list(ft_map(square, test_list)))
