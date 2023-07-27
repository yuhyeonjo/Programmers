def solution(a, b):
    answer = 0
    if a >= b :
        temp = range(b, a+1)
    else : temp = range(a, b+1)
    answer = sum(temp)
    return answer