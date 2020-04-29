# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/29 17:02:28 by vflander          #+#    #+#              #
#    Updated: 2020/04/29 17:02:28 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv

morse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}


def morse_encode(arg_list: list) -> str:
    """encodes strings into Morse code. The input will accept all
    alphanumeric characters. And prints ERROR is even a single char is not.
    :param arg_list: from sys.argv
    :return: encoded morse string
    """
    if len(argv) > 1:
        string = ' '.join(arg_list[1:])
    else:
        return ""
    # trimming extra spaces and checking for unwanted characters
    test_list = string.split()
    for word in test_list:
        if not word.isalnum():
            return "ERROR"
    string = ' '.join(test_list).lower()
    # string is good, encoding now
    result = ""
    for i in range(len(string)):
        if i != 0:
            result += " "
        if string[i] == " ":
            result += "/"
            continue
        result += morse[string[i]]
    return result


if __name__ == "__main__":
    print(morse_encode(argv))
