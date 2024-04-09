#!/usr/bin/python3
def validUTF8(data):
    
    remaining_bytes = 0
    
    
    for byte in data:
        
        if remaining_bytes > 0:
            if byte >> 6 != 0b10:
                return False
            remaining_bytes -= 1
        else:
            
            mask = 0b10000000
            while byte & mask:
                remaining_bytes += 1
                mask >>= 1
            
            
            if remaining_bytes == 0:
                if byte >> 7 == 0:
                    continue
                else:
                    return False
            elif remaining_bytes > 4 or remaining_bytes == 1:
                return False
            
        
        remaining_bytes -= 1
    
    
    return remaining_bytes == 0

