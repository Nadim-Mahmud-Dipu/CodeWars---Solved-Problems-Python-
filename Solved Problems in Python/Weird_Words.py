def next_letter(s):
    result = ""
    
    for i in s:
        if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) and (i!='z' and i!='Z'):
            x = chr(ord(i) + 1)
            result+=x
        
        else:
            if i =='z':
                result+='a'
            elif i == 'Z':
                result+= 'A'
            else:
                result+=i
            
    ans = ""
    for j in result:
        if j=='[':
            ans+='A'
        else:
            ans+=j
    
    return ans
