def solution(t, p):
    answer = list(t)
    temp = []
    count = 0
    for i in range(len(answer)) :
        if(len(answer[i:i+len(p)]) == len(p)) :
            temp.append(answer[i:i+len(p)])
        else : break
    
    for num in temp :
        if int("".join(num)) <= int(p) :
            count += 1
    
    
    return count