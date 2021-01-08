def variance(numbers): 
    # your code here
    mean = sum(numbers)/len(numbers)
    
    x = 0
    
    for i in numbers:
        x+= (mean - i) ** 2
    
    return x/len(numbers)