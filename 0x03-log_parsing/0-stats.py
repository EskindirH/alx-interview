import sys
import signal
import re

# Regular expression pattern to match the valid input format
LOG_PATTERN = re.compile(
    r'(\S+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
)

# Initialize variables
total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_statistics():
    """Print statistics about total file size and status codes."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")


def handle_interrupt(signal, frame):
    """Handle KeyboardInterrupt to print statistics and exit."""
    print_statistics()
    sys.exit(0)


# Attach signal handler for keyboard interrupt
signal.signal(signal.SIGINT, handle_interrupt)

# Process lines from stdin
try:
    for line in sys.stdin:
        match = LOG_PATTERN.match(line)
        if match:
            # Extract status code and file size
            status_code = int(match.group(2))
            file_size = int(match.group(3))

            # Update total file size
            global total_file_size
            total_file_size += file_size

            # Update status code count if it is a valid code
            if status_code in status_code_count:
                status_code_count[status_code] += 1

            # Increment line count and print statistics every 10 lines
            line_count += 1
            if line_count % 10 == 0:
                print_statistics()

except Exception as e:
    print(f"Error occurred: {e}")

# Print final statistics if the script ends naturally
print_statistics()
