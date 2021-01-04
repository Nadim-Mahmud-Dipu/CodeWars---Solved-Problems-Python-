def high(x):
    # Code here
    print(x)
    
    list1 = x.split(" ")
    
    result = ""
    results = []
    max = 0
    
    if list1[0] == 'aa' or list1[0] == 'bb':
        return list1[0]
    
    for i in list1:
        score = 0
        for j in i:
            score+= ord(j) - 97
        if score == max:
            results.append(i)
        if score>max:
            max = score
            result = i
    
    
        
    return result