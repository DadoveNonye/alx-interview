#!/usr/bin/python3
from collections import defaultdict

def parse_line(line):
  """Parses a line in the expected format and extracts file size.

  Args:
      line: A string representing a line from standard input.

  Returns:
      The extracted file size as an integer or None if the line format is invalid.
  """
  try:
    # Split the line based on spaces (ignoring extra spaces)
    parts = line.strip().split()
    if len(parts) < 6:
      return None
    # Assuming file size is the last element
    return int(parts[-1])
  except (ValueError, IndexError):
    return None

def main():
  """Reads lines from standard input, computes metrics, and prints statistics."""
  total_size = 0
  status_code_counts = defaultdict(int)
  line_count = 0

  try:
    for line in iter(input, ""):
      # Process the line
      file_size = parse_line(line)
      if file_size is not None:
        total_size += file_size
        line_count += 1
        status_code_counts[int(line.split()[3])] += 1

      # Print statistics every 10 lines or on keyboard interrupt
      if line_count % 10 == 0 or line_count == 1:
        print(f"Total file size: {total_size}")
        for code, count in sorted(status_code_counts.items()):
          print(f"{code}: {count}")
        print()  # Add an empty line for better readability

  except KeyboardInterrupt:
    print("\nKeyboard Interrupt received. Printing statistics:")
    print(f"Total file size: {total_size}")
    for code, count in sorted(status_code_counts.items()):
      print(f"{code}: {count}")

if __name__ == "__main__":
  main()
