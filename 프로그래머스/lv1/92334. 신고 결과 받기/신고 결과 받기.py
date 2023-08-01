import collections

def solution(id_list, report, k):
    answer = []
    report_list = []
#     id_list = dict.fromkeys(id_list, 0)

    # 신고한 이용자 ID 정보 문자열 배열 공백 나누기
    for i in list(set(report)) :
        temp = i.split(" ")
        report_list.append(temp)
    
#     # 유저별 신고당한 횟수 구하기
#     for report_name in report_list :
#         for key, value in id_list.items() :
#             if(key == report_name[1]) :
#                 id_list[key] += 1
    

    reportHash = collections.defaultdict(set)
    stoped = collections.defaultdict(int)
    
    for a in report_list :
        reportHash[a[0]].add(a[1])
        # stoped[b]+=1
    
    for b in reportHash :
        print(b)
    
    # print(reportHash)
    # print(stoped)
                
    
    return answer