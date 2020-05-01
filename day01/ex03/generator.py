# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/01 08:29:12 by vflander          #+#    #+#              #
#    Updated: 2020/05/01 08:29:12 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import shuffle

def generator(text: str, sep=" ", option=None) -> list:
    """Takes a text as input, uses the string 'sep' as a splitting parameter,
    and yields the resulting substrings.
    The function can take an optional argument. The options are:
    • “shuffle”: shuffle the list of words.
    • “unique”: return a list where each word appears only once.
    • “ordered”: alphabetically sort the words.
    :param text: str - input text
    :param sep: str - separator
    :param option: str - one of those {"shuffle", "unique", "ordered"}
    :return: yield next value, not returning the whole list
    """
    options_set = {"shuffle", "unique", "ordered"}
    try:
        output = text.split(sep)
    except AttributeError:
        # if need only basic error, keep only 1st line of strings
        error = "ERROR!"
        name = text.__class__.__name__
        error += f"\nInput text should be string, not '{name}'"
        # no yield for except block
        print(error)
        return
    if option == "shuffle":
        shuffle(output)
    elif option == "unique":
        # Starting with Python 3.7, the built-in dictionary
        # is guaranteed to maintain the insertion order
        output = dict.fromkeys(output)
    elif option == "ordered":
        output = sorted(output)
    elif option not in options_set and option:
        # if need only basic error, keep only 1st line of strings
        error = f"ERROR!"
        error += f"\nUnknown option \"{option}\"\n"
        error += f"Available options: {', '.join(options_set)}\n"
        yield error
    # output
    for word in output:
        yield word


if __name__ == "__main__":
    text = "5 4 3 0 0 1 1 2"
    print("TESTING EMPTY")
    for item in generator(text, sep=" "):
        print(item, end=' ')
    print("\nTESTING UNKNOWN")
    for item in generator(text, option="42"):
        print(item, end=' ')
    print("\nTESTING BAD TEXT")
    for item in generator(1):
        pass
    for item in generator(["1", "12", "123"]):
        pass
    for item in generator({"key": "value"}):
        pass
    print("\nTESTING ORDERED")
    for item in generator(text, option="ordered"):
        print(item, end=' ')
    print("\nTESTING SHUFFLE")
    for item in generator(text, option="shuffle"):
        print(item, end=' ')
    print("\nTESTING UNIQUE")
    for item in generator(text, option="unique"):
        print(item, end=' ')
