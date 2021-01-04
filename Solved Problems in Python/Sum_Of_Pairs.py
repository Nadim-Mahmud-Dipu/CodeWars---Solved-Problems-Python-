def sum_pairs(ints, s):
    cache = []
    for i in range(1,len(ints)):
        
        if ints[i] in cache:
            continue
        cache.append(ints[i])
        
        slice = ints[:i]
        
        x = s - ints[i] 
        if x in slice:
            return [x,ints[i]]
           
        