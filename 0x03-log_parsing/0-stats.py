#!/usr/bin/python3
import sys
import re
import signal

# Initialize variables to store total file size and status code counts
total_size = 0
status_codes_count = {code: 0 for code in [200, 301, 400, 401,
                        403, 404, 405, 500]}
line_count = 0

def signal_handler(sig, frame):
    """Handle CTRL + C signal to exit gracefully."""
    print_statistics()
    sys.exit(0)

def print_statistics():
    """Print the current statistics for total file size and status codes."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes_count):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))

def process_log_line(line):
    """Process a single log line, updating total
    size and status code counts."""
    global total_size, line_count
    line_count += 1

    # Split the regex pattern across multiple lines
    log_pattern = re.compile(
        r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] '
        r'"GET /projects/260 HTTP/1.1" '
        r'(\d{3}) (\d+)'
    )
    
    match = log_pattern.match(line)

    if match:
        status_code = int(match.group(3))
        file_size = int(match.group(4))
        total_size += file_size

        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        # Print statistics every 10 valid lines
        if line_count % 10 == 0:
            print_statistics()

def main():
    """Main function to read log entries from stdin and process them."""
    signal.signal(signal.SIGINT, signal_handler)  # Register signal handler

    try:
        for line in sys.stdin:
            process_log_line(line)

    except KeyboardInterrupt:
        print_statistics()

    except Exception as e:
        print("An error occurred: {}".format(e))
        sys.exit(1)

    # Print final statistics at the end
    print_statistics()

if __name__ == "__main__":
    main()
