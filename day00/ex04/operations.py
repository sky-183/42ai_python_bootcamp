# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/29 12:36:22 by vflander          #+#    #+#              #
#    Updated: 2020/04/29 12:36:22 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv


def args_is_good(arg_list: list) -> bool:
    """Check arguments for validity and prints appropriate responses
    :param arg_list: list of params
    :return: True if have 2 arguments, both are int
    """
    usage_msg = (
        "Usage: python operations.py <number1> <number2>\n"
        "Example:\n"
        "    python operations.py 10 3\n"
    )
    too_many_msg = "InputError: too many arguments\n"
    only_numbers_msg = "InputError: only numbers\n"
    if len(arg_list) == 1:
        print(usage_msg)
        return False
    if len(arg_list) > 3:
        print(too_many_msg, usage_msg)
        return False
    try:
        a, b = int(arg_list[1]), int(arg_list[2])
        # discarding floats here, even those like 5.0
        # use float.is_integer() if need to keep those
        # keeping only 42 or "42" (ints with or without quotes)
        if arg_list[1] == str(a) and arg_list[2] == str(b):
            return True
    except TypeError:
        print(only_numbers_msg, usage_msg)
        return False


def operations(arg_list: list):
    """Prints the results of the four elementary mathematical operations
    of arithmetic (addition, subtraction, multiplication, division)
    and the modulo operation. The result is formatted like this:

    > python operations.py 42 10
    Sum:        52
    Difference: 32
    Product:    420
    Quotient:   4.2
    Remainder:  2

    Takes list of parameters and checks for its validity before
    attempting operations.

    :param arg_list: params from command line
    """
    if not args_is_good(arg_list):
        return
    a, b = int(arg_list[1]), int(arg_list[2])
    operation_names = (
        "Sum",
        "Difference",
        "Product",
        "Quotient",
        "Remainder"
    )
    result_list = [
        a + b,
        a - b,
        a * b,
        "ERROR (div by zero)" if b == 0 else a / b,
        "ERROR (modulo by zero)" if b == 0 else a % b
    ]
    for name, result in zip(operation_names, result_list):
        print(f"{name:<12}{result}")


if __name__ == "__main__":
    operations(argv)
