import collections

def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    reportHash = collections.defaultdict(set)
    stoped = collections.defaultdict(int)
    
    # 유저별 신고한 ID와 신고 횟수 구하기 
    for x in report :
        a, b = x.split(" ")
        reportHash[a].add(b)
        stoped[b]+=1
        
    # 신고 횟수 구하기
    for name in id_list :
        count = 0
        for user in reportHash[name] :        
            if(stoped[user] >= k) :
                count += 1
        answer.append(count)
    return answer