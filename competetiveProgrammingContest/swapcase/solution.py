def swap_case(s):
    swapCase = ""
    
    for c in s:
        if c.islower():
            swapCase += c.upper()
            
        else:
            swapCase += c.lower()
            
    return swapCase
    
