# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/30 08:50:10 by vflander          #+#    #+#              #
#    Updated: 2020/04/30 08:50:10 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

if __name__ == "__main__":
    print("TEST INIT")
    print(Vector(5))
    print(Vector("not_int"))
    print(Vector("4"))
    print(Vector(1, 5))
    print(Vector(["1"]))
    print(Vector({1, 3}))
    print(Vector(["one", "two"]))
    print(Vector([]))
    print(Vector([3]))
    print(Vector([4, 5]))
    # operations testing
    print("TESTING OPERATIONS")
    vec1 = Vector(5)
    vec2 = Vector(5, 10)
    vec3 = Vector([1, 3, 0])
    print(repr(vec1))
    print(repr(vec2))
    print("TEST ADD")
    print(vec1 + vec2)
    print(vec2 + vec1)
    print(vec1 + vec3)
    print(vec1 + 15)
    print(vec1 + "10")
    print(vec1 + [0, 1, 2, 3, 4])
    print(15 + vec1)
    print("TEST SUB")
    print(vec1 - vec2)
    print(vec2 - vec1)
    print(vec1 - 42)
    print(42 - vec1)
    print(vec1 - "10")
    print("TEST MUL")
    print(vec1 * vec2)
    print(vec2 * vec1)
    print(vec1 * vec3)
    print(vec1 * 10)
    print(vec1 * -1)
    print(-1 * vec1)
    print(vec1 * "10")  # yes, this is working
    print(vec1 * {42})
    print(vec1 * [42])
    print("TEST TRUEDIV")
    print(vec1 / vec2)
    print(vec1 / vec3)
    print(vec1 / 2)
    print(2 / vec1)
    print(vec1 / "10")  # yes, this is working
    print(vec1 / {42})
    print(vec1 / [42])
