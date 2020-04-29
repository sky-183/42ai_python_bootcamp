# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/29 12:36:10 by vflander          #+#    #+#              #
#    Updated: 2020/04/29 12:36:10 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from string import punctuation


def text_analyzer(text=None):
    """prints the number of characters, upper characters, lower characters,
    punctuation marks and spaces in a given text. If there is no text passed
    to the function, the user is prompted to give one.
    :param text: text to analyze
    """
    if text is None:
        text = input("What is the text to analyse?\n")
    upper_case_letters = 0
    lower_case_letters = 0
    punctuations_marks = 0
    spaces = 0
    for char in text:
        if char.isupper():
            upper_case_letters += 1
            continue
        if char.islower():
            lower_case_letters += 1
            continue
        # to count all space-like symbols, use .isspace instead
        if char == " ":
            spaces += 1
            continue
        if char in punctuation:
            punctuations_marks += 1
            continue
        # can print or count unexpected chars here
    # formatting result
    result_tuple = (
        f"The text contains {len(text)} characters:",
        f"- {upper_case_letters} upper letters",
        f"- {lower_case_letters} lower letters",
        f"- {punctuations_marks} punctuation marks",
        f"- {spaces} spaces"
        )
    result = "\n".join(result_tuple)
    # using 'print' here instead of 'return' to work ok in python shell
    # (which uses real string, not its representation (as print does))
    # as shown in examples
    print(result)


if __name__ == "__main__":
    test_string = """
    Python is an interpreted, high-level, general-purpose programming language.
    Created by Guido van Rossum and first released in 1991, Python's design
    philosophy emphasizes code readability with its notable use of significant
    whitespace.
    """
    text_analyzer(test_string)
    text_analyzer()
