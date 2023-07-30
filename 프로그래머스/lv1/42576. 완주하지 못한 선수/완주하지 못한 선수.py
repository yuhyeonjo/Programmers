def solution(participant, completion):
    answer = ''
    hashDict={}
    sumHash=0
    for part in participant:
        hashDict[hash(part)]=part
        sumHash+=hash(part)
    
    
    for comp in completion:
        sumHash-=hash(comp)
    # 첫 번째 풀이 방법 : 시간초과발생
#     temp_dict = dict(zip(participant, [0]*len(participant)))

#     for name in participant :
#         if(name in participant) :
#             temp_dict[name] += 1       
    
#     for name in completion : 
#         if(name in temp_dict) :
#             temp_dict[name] -= 1
    
    
#     for key,value in temp_dict.items() :
#         if(value != 0) :
#             answer += key
    
        
    return hashDict[sumHash]