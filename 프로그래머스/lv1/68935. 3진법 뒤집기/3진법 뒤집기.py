import math

def solution(n):
    answer = 0
    temp = ''
    
    while(n > 0) :
        n, mod = divmod(n, 3)
        temp += str(mod)
    
    temp = list(str(int(temp)))
    temp = temp[::-1]
    print(temp)
    for idx, value in enumerate(temp) :
        answer += math.pow(3, idx) * int(value)
    return answer