def comp(array1, array2):
    print(array1,array2)
    if array2 == None or array1 == None:
        return False
    if len(array1) == 0 and len(array2)!=0:
        return False
    if len(array2) == 0 or len(array1) == 0:
        return True
    
    array1 = [x*x for x in array1]
    
    flag = False
    
    for i in array2:
        if i in array1:
            flag = True
            array1.remove(i)
        else:
            flag = False
            break
            
    return flag