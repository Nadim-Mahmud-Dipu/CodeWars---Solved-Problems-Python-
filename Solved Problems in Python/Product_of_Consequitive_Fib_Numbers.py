import math
def productFib(prod):
    # your code
    
    x = 0
    y = 1
    
    fib = [x,y]
    
    for i in range(500):
        z = x+y
        fib.append(z)
        x = y
        y = z
        
    answer = []
    
    for i in range(1,len(fib)):
        x = fib[i] * fib[i-1]
        if x == prod:
            answer = [fib[i-1],fib[i],True]
            break
        
        if x> prod:
            answer = [fib[i-1],fib[i],False]
            break
        
            
    return answer