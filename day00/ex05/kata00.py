# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/29 12:34:55 by vflander          #+#    #+#              #
#    Updated: 2020/04/29 12:34:55 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == "__main__":
    t = (19, 42, 21)
    print(f"The {len(t)} numbers are: " + ', '.join(map(str, t)))