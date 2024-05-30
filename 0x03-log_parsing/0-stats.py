#!/usr/bin/python3
"""
log parsing
"""

import sys
import signal
import re

# Initialize metrics
total_size = 0
status_codes_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0}
line_count = 0


def print_stats():
    """Print the statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def signal_handler(sig, frame):
    """Handle the interrupt signal."""
    print_stats()
    sys.exit(0)


# Register the signal handler for keyboard interrupt
signal.signal(signal.SIGINT, signal_handler)

# Regular expression to match the log format
log_pattern = re.compile(
    r'^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

try:
    while True:
        try:
            line = input()
            match = log_pattern.match(line)
            if match:
                # Extract fields
                status_code = int(match.group(3))
                file_size = int(match.group(4))

                # Update metrics
                total_size += file_size
                if status_code in status_codes_count:
                    status_codes_count[status_code] += 1

                line_count += 1

                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_stats()
        except EOFError:
            break
except KeyboardInterrupt:
    pass
finally:
    print_stats()
