def solution(s):
    answer = ''
    temp_str = s.split(" ");
    for i in temp_str :
        count = 0
        for j in i :
            count += 1
            if(count % 2 == 1) :
                j = j.upper()
            else :
                j = j.lower()
            answer += j
        answer += " "
    answer = answer[:-1]
    return answer