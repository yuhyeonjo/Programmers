def solution(n):
    answer = []
    temp = list(str(n))
    temp = temp[::-1]
    for i in temp :
        answer.append(int(i))
    return answer