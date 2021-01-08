def arrange(string):
    # your code
    
    words = list(string.split())
    
    for i in range(len(words)-1):
        if i == 0 or i%2==0:
            if len(words[i]) > len(words[i+1]):
                words[i], words[i+1] = words[i+1], words[i]
                words[i] = words[i].upper()
        else:
            if len(words[i]) < len(words[i+1]):
                words[i], words[i+1] = words[i+1], words[i]
                words[i] = words[i].lower()
    str1=""
    for i in range(len(words)):
        if i == 0 or i%2==0:
            str1+= words[i].lower()+ " "
        else:
            str1+= words[i].upper()+ " "
    return str1[:-1]