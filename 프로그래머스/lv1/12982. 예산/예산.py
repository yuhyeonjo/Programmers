def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)) :
        if(sum(d) > budget) :
            d.pop()
        else :
            break
    answer = len(d)
    return answer