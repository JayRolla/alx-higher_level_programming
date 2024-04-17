#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
It calculates the total file size and the count of each HTTP status code.
Handles:
- Single line logs.
- Logs with only one type of status code.
- Logs with up to 10 lines, more than 10 lines, and empty input.
- Improperly formatted log entries.
Output statistics every 10 lines or at the end of input.
"""

def print_stats(total_size, status_codes):
    """Print accumulated log statistics."""
    print("File size: {}".format(total_size))
    for status in sorted(status_codes):
        if status_codes[status] > 0:
            print("{}: {}".format(status, status_codes[status]))

def process_log():
    """Process logs from standard input."""
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    line_count = 0

    try:
        while True:
            line = input()
            if line.strip() == "":
                continue  # handle empty lines in input

            try:
                parts = line.split()
                status = parts[-2]
                size = int(parts[-1])
                if status in status_codes:
                    status_codes[status] += 1
                    total_size += size
            except (IndexError, ValueError):
                continue  # handle wrong format lines

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except EOFError:
        pass
    finally:
        if line_count > 0:
            print_stats(total_size, status_codes)

if __name__ == "__main__":
    process_log()
