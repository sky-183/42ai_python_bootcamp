# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/29 12:35:09 by vflander          #+#    #+#              #
#    Updated: 2020/04/29 12:35:09 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == "__main__":
    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
    }
    for key, value in languages.items():
        print(f"{key} was created by {value}")
