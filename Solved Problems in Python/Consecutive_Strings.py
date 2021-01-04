def longest_consec(strarr, k):
    #print(strarr,k)
    # your code
    stack = []
    
    if len(strarr) == 0:
        return ""
    
    if k <= 0:
        return ""
    if k> len(strarr):
        return ""
    
    for i in range(len(strarr)-k+1):
        str = strarr[i]
        
        for j in range(k-1):
            i+=1
            str+= strarr[i]
        stack.append(str)
        
    if k == 1:
        stack = strarr
     
    x = [len(i) for i in stack]
    
    if len(stack) == 0:
        return ""
    maximum = max(x)
    #print(stack)
    for i in range(len(stack)):
        if len(stack[i]) == maximum:
            return stack[i]
    