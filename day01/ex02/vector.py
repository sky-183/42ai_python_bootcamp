# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/30 08:50:00 by vflander          #+#    #+#              #
#    Updated: 2020/04/30 08:50:00 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
The official documentation for vector module
"""


class Vector:
    """Vector (list of floats), which can perform other operations
    with another vectors and scalars
    """
    def __init__(self, *args):
        error = ("ERROR!\n"
                 "Initialise vector with 1 or 2 ints or with list of floats"
                 )
        self.values = None
        try:
            if len(args) == 1:
                # if 1 argument and it's a int or valid str(int)
                if isinstance(args[0], list):
                    # print("initialising with list")
                    # skipping empty lists
                    if len(args[0]) > 0:
                        self.values = [float(x) for x in args[0]]
                    else:
                        raise TypeError
                elif str(int(args[0])) == args[0] or isinstance(args[0], int):
                    # print("initialising with single int (range)")
                    self.values = [float(x) for x in range(int(args[0]))]
                else:
                    raise TypeError
            elif len(args) == 2:
                if isinstance(args[0], int) and isinstance(args[1], int):
                    # print("initialising with 2 ints (range)")
                    self.values = [float(x) for x in range(args[0], args[1])]
                else:
                    raise TypeError
            else:
                raise TypeError
        except (TypeError, ValueError):
            # will create class object every time (Null on errors), since we're
            # catching all exceptions instead of letting user of the class
            # do it when he really needs it
            print(error)
        self.size = 0 if not self.values else len(self.values)
        # self.size = len(self.values)
        # print(f"Vector created successfully: {self.values}")

    def __repr__(self):
        """All useful details for class object"""
        return f"{self.__class__}, {self.__dict__}"

    def __str__(self):
        """Pretty readable printing"""
        return f"vector {self.values}"

    def __add__(self, other):
        if isinstance(other, Vector):
            if self.size == other.size:
                return [a + b for a, b in zip(self.values, other.values)]
            else:
                return "ERROR! Cannot add vectors with different sizes"
        else:
            # if we'll decide we can add vector and scalar it could look like
            # return [float(other) + x for x in self.values]
            name = other.__class__.__name__
            return f"ERROR! Cannot add vector and {name}, only with vectors"

    def __sub__(self, other):
        if isinstance(other, Vector):
            if self.size == other.size:
                return [a - b for a, b in zip(self.values, other.values)]
            else:
                return "ERROR! Cannot subtract vectors with different sizes"
        else:
            name = other.__class__.__name__
            return f"ERROR! Cannot subtract vector with {name}, only with vectors"

    def __mul__(self, other):
        if isinstance(other, Vector):
            if self.size == other.size:
                return sum([a * b for a, b in zip(self.values, other.values)])
            else:
                return "ERROR! Cannot multiply vectors with different sizes"
        try:
            return [float(other) * x for x in self.values]
        except (TypeError, ValueError):
            name = other.__class__.__name__
            return f"ERROR! Cannot multiply vector on {name}, only on scalars"

    def __truediv__(self, other):
        try:
            return [x / float(other) for x in self.values]
        # dont need to catch ZeroDivisionError
        except (TypeError, ValueError):
            name = other.__class__.__name__
            return f"ERROR! Cannot divide vector on {name}, only on scalars"

    __rsub__ = __sub__
    __radd__ = __add__
    __rmul__ = __mul__
    __rtruediv__ = __truediv__


if __name__ == "__main__":
    pass
