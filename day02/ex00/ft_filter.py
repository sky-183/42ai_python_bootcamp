# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/02 18:10:52 by vflander          #+#    #+#              #
#    Updated: 2020/05/02 18:10:52 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_filter(function_to_apply, list_of_inputs):
    """Construct iterator for those elements of input iterator, for which
    given function returns True.
    :param function_to_apply:   returns True/False
    :param list_of_inputs:      iterable
    :return:                    iterable
    """
    return (item for item in list_of_inputs if function_to_apply(item))


if __name__ == "__main__":
    test_list = list(range(-5, 5))
    print(list(ft_filter(lambda x: x > 0, test_list)))
