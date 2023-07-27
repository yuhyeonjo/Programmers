def solution(arr, divisor):
    answer = []
    for i in arr :
        temp = i if i % divisor == 0 else 0
        if (temp != 0) : answer.append(temp)
    
    if(len(answer) == 0) :
        answer.append(-1)
        
    answer.sort()
    return answer