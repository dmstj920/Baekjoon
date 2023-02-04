from collections import defaultdict

def solution(id_list, report, k):
    reportHash = defaultdict(set)
    stopHash = defaultdict(int)
    
    for i in report:
        reportString = i.split()
        reportHash[reportString[0]].add(reportString[1])
        stopHash[reportString[1]] += 1
    
    """
    for key in reportHash.keys():
        for j in reportHash.get(key):
            stopHash[j] += 1
    """
        
    answer = []
    for name in id_list:
        mail = 0
        for user in reportHash[name]:
            if stopHash[user] >= k:
                mail += 1
                
        answer.append(mail)
    
    return answer
