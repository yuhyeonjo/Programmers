import math
def solution(s):
    answer = ''
    # 단어 길이 홀수면 한글자, 짝수면 두글자
    num = 1 if len(s) % 2 == 1 else 2
    start = math.ceil(len(s) / 2) - 1
    
    temp_list = list(s)
    sliced_list = temp_list[start:start+num]
    answer = "".join(sliced_list)
    return answer