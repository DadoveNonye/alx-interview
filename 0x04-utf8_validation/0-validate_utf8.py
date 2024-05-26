#!/usr/bin/python3
def validUTF8(data):
  """
  Checks if the given data represents a valid UTF-8 encoding.

  Args:
      data: A list of integers representing bytes of data.

  Returns:
      True if the data is a valid UTF-8 encoding, False otherwise.
  """
  count_ones = 0
  for byte in data:
    # Extract the 8 least significant bits
    byte = byte & 0b11111111

    # Check for valid byte based on number of continuation bytes:
    if count_ones == 0:
      if byte >= 0xc0:  
        count_ones = 1
      elif byte >= 0xe0:  
        count_ones = 2
      elif byte >= 0xf0:  
        count_ones = 3
      elif byte >= 0x80:  
        return False
    else:
      if byte & 0xc0 != 0x80:  
        return False
      count_ones -= 1

  return count_ones == 0 