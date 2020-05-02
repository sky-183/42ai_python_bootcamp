# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/02 19:15:55 by vflander          #+#    #+#              #
#    Updated: 2020/05/02 19:15:55 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from time import sleep, time
from random import randint
from functools import wraps
from getpass import getuser


def log(func):
    # for returning correct name from the wrapped function
    @wraps(func)
    def wrapped(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        running = end - start
        log = f"({getuser()})Running: "
        name = " ".join(map(str.capitalize, func.__name__.split("_")))
        log += f"{name:16}"
        log += "[ exec-time = "
        if running < 1:
            log += f"{(running * 1000):7.3f} ms ]\n"
        else:
            log += f"{running:7.3f} s  ]\n"
        # print(log)
        with open('machine.log', 'a+') as f:
            f.write(log)
        return result
    return wrapped


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)

