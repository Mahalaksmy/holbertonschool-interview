#!/usr/bin/python3
"""This is script that reads stdin element by element and computes metrics:"""

import sys

if __name__ == "__main__":

    datas = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    file_size = [0]
    count = 1

    def print_stats():
        '''
        Prints file size and stats for every 10 loops
        '''
        print('File size: {}'.format(file_size[0]))

        for code in sorted(param.keys()):
            if param[code] != 0:
                print('{}: {}'.format(code, param[code]))

    def parse_stdin(param):
        '''
        Checks the stdin for matches
        '''
        try:
            param = param[:-1]
            word = param.split(' ')

            file_size[0] += int(word[-1])

            data = int(word[-2])

            if data in param:
                param[data] += 1
        except BaseException:
            pass

    try:
        for param in sys.stdin:
            parse_stdin(line)

            if count % 10 == 0:
                print_stats()
            count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
    