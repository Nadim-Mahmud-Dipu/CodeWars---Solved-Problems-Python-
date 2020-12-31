def score(dice):
    # your code here
    print(dice)
    result = 0
    
    one = dice.count(1)
    two = dice.count(2)
    three = dice.count(3)
    four = dice.count(4)
    five = dice.count(5)
    six = dice.count(6)
    
    if one>=3:
        result+=1000
        result+= (one-3) * 100
    if six>=3:
        result+=600
    if five>=3:
        result+=500
        result+= (five-3)*50
    if four>=3:
        result+=400
    if two>=3:
        result+=200
    if three>=3:
        result+=300
    
    if one<3:
        result+=one*100
    if five<3:
        result+=five*50
    return result