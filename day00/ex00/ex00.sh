# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    answers.sh                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/29 06:53:15 by vflander          #+#    #+#              #
#    Updated: 2020/04/29 06:53:15 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/sh

# output to file
FILE="output_answers.txt"

# 1) installed python packages
pip list | cut -d' ' -f1 > $FILE

# 2) installed python packages and their version
echo "\n" >> $FILE
pip list >> $FILE

# 3) show the package metadata for numpy
echo "\n" >> $FILE
pip show numpy >> $FILE

# 4) search for PyPI packages whose name or summary contains "tesseract"
echo "\n" >> $FILE
pip search "tesseract" >> $FILE

# 5) freeze the packages and their current versions in a requirements.txt
echo "\n" >> $FILE
pip freeze >> $FILE

