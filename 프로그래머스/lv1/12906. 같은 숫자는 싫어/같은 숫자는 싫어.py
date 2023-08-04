import collections

def solution(arr):
    answer = []
    answer.append(arr[0])
    for idx, value in enumerate(arr) :
        if idx == 0: 
            continue
        elif arr[idx-1] == arr[idx] :
            continue
        else : answer.append(value)
    return answer