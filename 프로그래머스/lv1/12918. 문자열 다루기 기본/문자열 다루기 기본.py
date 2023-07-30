def solution(s):
    answer = False

    if(len(s) == 4 or len(s) ==6) :
        answer = True
        try :
            int(s)
        except :
            answer = False
    return answer