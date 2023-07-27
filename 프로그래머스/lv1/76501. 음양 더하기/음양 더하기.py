def solution(absolutes, signs):
    temp_list = []
    for i in range(len(absolutes)) :
        num = 1 if signs[i] == True else -1 
        temp_list.append(absolutes[i] * num)
    
    answer = sum(temp_list)
    return answer