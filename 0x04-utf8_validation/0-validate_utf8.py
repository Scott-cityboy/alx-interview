#!/usr/bin/python3
def validUTF8(data):
    # Number of bytes remaining for a multibyte character
    remaining_bytes = 0
    
    # Iterate through each integer in the data set
    for byte in data:
        # Check if this byte is a continuation byte (starts with '10')
        if remaining_bytes > 0:
            if byte >> 6 != 0b10:
                return False
            remaining_bytes -= 1
        else:
            # Count the number of leading '1's to determine the number of bytes in the character
            mask = 0b10000000
            while byte & mask:
                remaining_bytes += 1
                mask >>= 1
            
            # Handle single-byte characters and check if remaining_bytes is within valid range
            if remaining_bytes == 0:
                if byte >> 7 == 0:
                    continue
                else:
                    return False
            elif remaining_bytes > 4 or remaining_bytes == 1:
                return False
            
        # Decrement remaining_bytes to indicate the current byte has been processed
        remaining_bytes -= 1
    
    # If there are remaining bytes, it indicates incomplete character
    return remaining_bytes == 0

