#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""

import sys

def compute_metrics(lines):
    """
    A function that computes the metrics
    """
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    
    for line in lines:
        parts = line.split()
        if len(parts) == 7 and parts[3].isdigit() and parts[4].isdigit():
            total_size += int(parts[4])
            status_code = int(parts[5])
            if status_code in status_counts:
                status_counts[status_code] += 1
    
    return total_size, status_counts

def print_statistics(total_size, status_counts):
    """
    A function that prints statistics
    """
    print(f"Total file size: {total_size}")
    for status_code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{status_code}: {count}")

def main():
    """
    Main function
    """
    lines = []
    try:
        for line in sys.stdin:
            lines.append(line.strip())
            if len(lines) == 10:
                total_size, status_counts = compute_metrics(lines)
                print_statistics(total_size, status_counts)
                lines = []
    except KeyboardInterrupt:
        total_size, status_counts = compute_metrics(lines)
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()
