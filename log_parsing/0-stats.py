#!/usr/bin/python3
"""Log parsing script: reads stdin and computes metrics."""
import sys
import re


def print_stats(total_size, status_codes):
    """Print the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """Read stdin line by line and compute metrics."""
    total_size = 0
    count = 0
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }

    pattern = re.compile(
        r'^\S+ - \[.*\] "GET /projects/260 HTTP/1\.1" (\S+) (\d+)$'
    )

    try:
        for line in sys.stdin:
            match = pattern.match(line.rstrip("\n"))
            if not match:
                continue

            code = match.group(1)
            size = int(match.group(2))

            total_size += size
            if code in status_codes:
                status_codes[code] += 1

            count += 1
            if count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
