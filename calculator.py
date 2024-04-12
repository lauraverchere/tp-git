def addition (a,b) : 
    # Addition function
    result = a + b 
    return result

def soustraction (a,b) : 
    # Substraction function
    result = a-b
    return result

def division (a, b) : 
    # Division function
    if b != 0 : 
        result = a /b 
    else :
        result = "Impossible to divide by zero"
    return result
