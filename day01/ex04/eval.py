# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/01 09:53:26 by vflander          #+#    #+#              #
#    Updated: 2020/05/01 09:53:26 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
This is the official doc for Evaluator class
"""


class Evaluator:
    """Has two static functions named: zip_evaluate and enumerate_evaluate.
    The goal of these functions is to compute the sum of the lengths of every
    words of a given list weighted by a list a coefs.
    The lists coefs and words have to be the same length.
    If this is not the case, the function should return -1.
    """
    # forbidden functions: while
    @staticmethod
    def zip_evaluate(coefs: list, words: list) -> int:
        """Compute the sum of the lengths of every words of a given list
        weighted by a list a coefs. The lists coefs and words have to be the
        same length. If this is not the case, the function should return -1.
        :param words: list of str
        :param coefs: list of float
        :return: int - result (or -1 in case of wrong list sizes)
        """
        if len(words) != len(coefs):
            return -1
        # result = 0
        # for word, coef in zip(words, coefs):
        #     result += word * coef
        result = sum([len(word) * coef for word, coef in zip(words, coefs)])
        return result

    @staticmethod
    def enumerate_evaluate(coefs: list, words: list) -> int:
        """Compute the sum of the lengths of every words of a given list
        weighted by a list a coefs. The lists coefs and words have to be the
        same length. If this is not the case, the function should return -1.
        :param words: list of str
        :param coefs: list of float
        :return: int - result (or -1 in case of wrong list sizes)
        """
        if len(words) != len(coefs):
            return -1
        # result = 0
        # for index, element in enumerate(words):
        #     result += len(element) * coefs[index]
        result = sum([len(word) * coefs[i] for i, word in enumerate(words)])
        return result


if __name__ == "__main__":
    """
    my_words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    my_coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(my_coefs, my_words))
    print(Evaluator.enumerate_evaluate(my_coefs, my_words))
    print(Evaluator.zip_evaluate(my_coefs, ["42"]))
    """
    pass
