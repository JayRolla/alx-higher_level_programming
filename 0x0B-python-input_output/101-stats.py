#!/usr/bin/python3
"""
Module for log parsing
"""

status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
total_size = 0
line_count = 0


def print_stats(signal_received=None, frame=None):
    """
    Prints the statistics since the beginning
    """
    global total_size, line_count

    print("File size: {:d}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{:s}: {:d}".format(code, count))


def parse_line(line):
    """
    Parses a single log line and updates the statistics
    """
    global total_size, line_count

    try:
        parts = line.split()
        ip_address = parts[0]
        date = parts[3][1:]
        status_code = parts[8]
        file_size = int(parts[9])

        total_size += file_size
        status_codes[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print_stats()
    except Exception:
        pass


def handle_signal(signal_received, frame):
    """
    Handles the CTRL+C signal and prints the final statistics
    """
    print_stats()
    exit(0)


if __name__ == "__main__":
    try:
        for line in iter(input, ""):
            parse_line(line.strip())
    except KeyboardInterrupt:
        handle_signal(None, None)
    print_stats()
