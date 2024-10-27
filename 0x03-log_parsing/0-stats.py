#!/usr/bin/python3

import sys
import re
import signal

# Initialize variables

total_size = 0
status_codes_count = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
        }
line_count = 0


def signal_handler(sig, frame):
    """Signal handler to handle keyboard interruption."""

    print_statistics()
    sys.exit(0)


def print_statistics():
    """Print the accumulated statistics."""

    print(f"File size: {total_size}")
    for status_code in sorted(status_codes_count):
        if status_codes_count[status_code] > 0:
            print("{}: {}".format(status_code,
                  status_codes_count[status_code]))


# Register the signal handler for SIGINT (CTRL + C)

signal.signal(signal.SIGINT, signal_handler)

# Regular expression pattern to match the log entry

pattern = (
    r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] '
    r'"GET /projects/260 HTTP/1.1" '
    r'(\d{3}) (\d+)'
    )

for line in sys.stdin:
    line_count += 1
    match = re.match(pattern, line)

    if match:

        # Extracting data from the matched line

        status_code = int(match.group(3))
        file_size = int(match.group(4))

        # Update total size and status codes count

        total_size += file_size
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        # Print statistics after every 10 lines

        if line_count % 10 == 0:
            print_statistics()
    else:
        continue

# Final statistics in case of end of input without interruption

print_statistics()
