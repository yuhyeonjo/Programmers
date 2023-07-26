def solution(n):
    temp = list(str(n))
    a = sorted(temp, reverse=True)
    b = ''
    for i in a :
        b += i
    answer = int(b)
    return answer