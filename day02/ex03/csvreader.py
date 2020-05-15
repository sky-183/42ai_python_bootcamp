# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/02 23:09:42 by vflander          #+#    #+#              #
#    Updated: 2020/05/02 23:09:42 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
CsvReader class main documentation lives here
"""
from os.path import exists
from os import close


class CsvReader():
    def __init__(self, path_to_file, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.sep = sep
        self.path_to_file = path_to_file
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.f = None

    def __enter__(self):
        try:
            self.f = open(self.path_to_file, 'r')
        except FileNotFoundError:
            print("ERROR! File not found.")
            return None
        self.f.seek(0)
        lines_list = self.f.readlines()
        row_len = len(lines_list[0].split(self.sep))
        # file is corrupter if has too many elements, return None
        for line in lines_list:
            if len(line.split(self.sep)) > row_len:
                return None
        result_list = []
        start_pos = self.header + self.skip_top
        end_pos = len(lines_list) - self.skip_bottom
        for i in range(start_pos, end_pos):
            this_line = list(map(str.strip, lines_list[i].split(self.sep)))
            result_list.append(this_line)
        # or just lines_list[start_pos : end_pos] if we're ok with strings
        self.data = result_list
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.f is not None:
            self.f.close()

    def getdata(self):
        return self.data

    def getheader(self):
        if self.header:
            self.f.seek(0)
            return list(map(str.strip, self.f.readline().split(self.sep)))
        else:
            return None


if __name__ == "__main__":
    with CsvReader('good.csv', header=True, skip_bottom=1, skip_top=1) as file:
        data = file.getdata()
        header = file.getheader()
        for line in data:
            print(line)
        print(header)
    with CsvReader('bad.csv') as file:
        if file is None:
            print("File is corrupted")
    with CsvReader('none.csv') as file:
        pass
