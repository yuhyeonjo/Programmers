def solution(x):
    numbers = list(map(int, list(str(x))))    
    result = x % sum(numbers)
    answer = True if result == 0 else False
    
    return answer