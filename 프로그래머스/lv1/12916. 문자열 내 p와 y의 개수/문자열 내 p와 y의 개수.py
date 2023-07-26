def solution(s):    
    pcount = s.count("p") + s.count("P")
    ycount = s.count("y") + s.count("Y")
    answer = True if pcount == ycount else False
    return answer