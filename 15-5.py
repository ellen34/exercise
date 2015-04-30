#factorial

def factorial(x):
    if x > 0:
        result = x * factorial(x-1)  
    elif x == 0:
        result= 1
    
    x -= 1
    return result
    
print factorial(7)
