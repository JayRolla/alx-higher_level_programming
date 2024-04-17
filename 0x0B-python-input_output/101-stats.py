#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics. Handles data formatted as:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Computes and prints the total file size and the count of each status code every 10 lines and/or upon a keyboard interruption (CTRL + C).
"""

def print_stats(total_size, status_codes):
    """Prints the total file size and the count of each status code."""
    print("File size: {}".format(total_size))
    for status in sorted(status_codes.keys()):
        print("{}: {}".format(status, status_codes[status]))

def process_log():
    """Processes log lines from standard input."""
    total_size = 0
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    line_count = 0

    try:
        while True:
            line = input()
            parts = line.split()
            status = parts[-2]
            size = int(parts[-1])
            if status in status_codes:
                status_codes[status] += 1
            total_size += size
            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except EOFError:
        pass
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)

if __name__ == "__main__":
    process_log()
