# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/29 15:41:29 by vflander          #+#    #+#              #
#    Updated: 2020/04/29 15:41:29 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from string import punctuation
from sys import argv


def short_words_filter() -> list:
    """removes all the words in a string that are shorter than or equal
    to n letters, and returns the filtered list with no punctuation.
    The program will accept only two parameters: a string, and an integer n.
    :return: list
    """
    if len(argv) != 3:
        return "ERROR"
    string = argv[1]
    # valid strings cannot have only digits (as in last example)
    if string.isdigit():
        return "ERROR"
    try:
        n = int(argv[2])
    except ValueError:
        return "ERROR"
    words_list = string.split(' ')
    words_list = [word.strip(punctuation) for word in words_list]
    words_list = [word for word in words_list if len(word) > n]
    return words_list


if __name__ == "__main__":
    print(short_words_filter())
