import math

def solution(n):
    answer = 0
    sqrt = math.sqrt(n)
    temp = int(sqrt) == sqrt
    
    answer = math.pow(int(sqrt) + 1, 2) if temp == True else -1
    return answer