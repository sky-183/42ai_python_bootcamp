# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/29 12:35:45 by vflander          #+#    #+#              #
#    Updated: 2020/04/29 12:35:45 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv


def rev_alpha(str_list: list) -> str:
    """You will have to make a program that reverses the order of a string and
    the case of its words. If we have more than one argument, we have to merge
    them into a single string and separate each arg by a ’ ’ (space char).
    :param str_list: list of strings 
    :return: resulting string
    """
    return " ".join(str_list[len(str_list):0:-1]).swapcase()


if __name__ == "__main__":
    print(rev_alpha(argv))
