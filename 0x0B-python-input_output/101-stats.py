#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""
import sys

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for status in sorted(status_codes.keys()):
        if status_codes[status]:
            print("{}: {}".format(status, status_codes[status]))

def process_log():
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) > 1:
                size = int(parts[-1])
                status = parts[-2]
                if status in status_codes:
                    status_codes[status] += 1
                total_size += size

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)

if __name__ == "__main__":
    process_log()
