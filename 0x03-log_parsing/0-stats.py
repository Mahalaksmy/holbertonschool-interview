#!/usr/bin/python3
"""This is script that reads stdin line by line and computes metrics:"""

import sys

data = {"Size": 0, "Codes": {"200": 0, "301": 0, "400": 0, "401": 0,
                             "403": 0, "404": 0, "405": 0, "500": 0}}


def printFormat():
    """Function that prints the file size and all the status codes"""

    print("File size: {}".format(data['Size']))

    for statusCode, count in sorted(data['Codes'].items()):
        if count != 0:
            print("{}: {}".format(statusCode, count))


if __name__ == "__main__":

    try:

        values = 1
        for line in sys.stdin:

            """Split the line taken from stdin and save only the needed data"""

            newValue = line.split(" ")
            try:
                size = int(newValue[-1])
                code = newValue[-2]

                """If the status code is a possible status code
                it will count + 1 in the dict to count how many of they are"""

                if code in data['Codes']:
                    data['Codes'][code] += 1

                data['Size'] += size
            except:
                pass

            if values % 10 == 0:
                printFormat()

            values += 1

    except KeyboardInterrupt:
        """Handling CTRL + C"""
        printFormat()
        raise

    printFormat()