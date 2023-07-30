def solution(numbers):
    sum_num = 0
    
    for i in range(0, 10) :
        sum_num += i
        
    sum_num = sum_num - sum(numbers)

    return sum_num