def solution(price, money, count):
    temp = 0;
    
    for i in range(1, count+1) :
        temp += i * price
    money -= temp
    money = 0 if money >= 0 else int(money) * (-1)
    
    return money