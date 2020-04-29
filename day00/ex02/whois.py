# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/29 12:35:58 by vflander          #+#    #+#              #
#    Updated: 2020/04/29 12:35:58 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv


def whois(str_list: list) -> str:
    """You will have to make a program that checks if a number is odd,
    even or zero. The program will accept only one parameter, an integer.
    Returns 'ERROR' on any errors (type on number of params)
    :param str_list: 
    :return: 
    """
    if len(argv) != 2:
        return "ERROR"
    # keep the integers in, but discard floats
    if argv[1][0] == "-":
        sign = -1
        argv[1] = argv[1][1:]
    else:
        sign = 0
    if not argv[1].isdigit():
        return "ERROR"
    # kinda irrelevant to keep sign here with current functionality
    num = sign * int(argv[1])
    if num == 0:
        return "I'm Zero"
    elif num % 2 == 0:
        return "I'm Odd"
    elif num % 2 == 1:
        return "I'm Even"
    else:
        return "You should not be here, traveller!"


if __name__ == "__main__":
    print(whois(argv))
