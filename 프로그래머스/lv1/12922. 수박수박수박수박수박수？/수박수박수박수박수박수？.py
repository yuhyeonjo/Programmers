def solution(n):
    answer = ''
    su = '수'
    bak = '박'
    
    for i in range(1, n+1) :
        if(i % 2 == 0) :
            answer += bak
        else : answer += su
    return answer