# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/02 23:17:14 by vflander          #+#    #+#              #
#    Updated: 2020/05/02 23:17:14 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from time import sleep, time
import sys


def ft_progress(my_list) -> list:
    time_start = time()
    bar_width = 20
    this_iter = 0  # for ETA
    for item in my_list:
        this_iter += 1
        percent = int((item / (len(my_list) - 1)) * 100)
        time_now = time()
        time_delta = time_now - time_start
        time_eta = abs(time_delta / this_iter * len(my_list) - time_delta)
        arrow_pos = int(percent / (100 / bar_width))
        bar = f"\rETA: {time_eta:.2f}s [{percent:3}%]"
        bar += f"[{'=' * (arrow_pos - 1)}>{' ' * (bar_width - arrow_pos - 1)}]"
        bar += f" {item + 1}/{len(my_list)} |"
        bar += f" elapsed time {time_delta:.2f}s"
        sys.stdout.write(bar)
        yield item


if __name__ == "__main__":
    print("test 1:")
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)
    print("test 2:")
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
    sleep(0.005)
    print()
    print(ret)
