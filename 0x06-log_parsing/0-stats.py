#!/usr/bin/python3
"""Log parsing"""

import sys


records = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
    }
file_size = 0
try:
    for time, line in enumerate(sys.stdin, 1):
        token = line.split()
        if len(token) > 2:
            status_code = token[len(token) - 2]
            file_size += int(token[len(token) - 1])
            if status_code in records:
                records[str(status_code)] += 1
        if time % 10 == 0:
            print("File size: {}".format(file_size))
            for sc in sorted(records):
                if records[sc] > 0:
                    print("{}: {}".format(sc, records[sc]))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(file_size))
    for sc in sorted(records):
        if records[sc] > 0:
            print("{}: {}".format(sc, records[sc]))
