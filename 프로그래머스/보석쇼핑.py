import collections

def solution(gems):
    jew = len(set(gems))
    sh = collections.defaultdict(int)
    answer = [0,0]
    shortest = [0,0]
    flag = 0
    shortLen = 100000
    
    lt, rt = 0, 0
    for rt in range(len(gems)):
        sh[gems[rt]] += 1
        while(len(sh) == jew):
            flag = 1
            shortest = [lt+1, rt+1]
            if shortLen > (shortest[1] - shortest[0] + 1):
                answer = shortest
            shortLen = min(shortLen, shortest[1] - shortest[0] + 1)
            sh[gems[lt]] -= 1
            if(sh[gems[lt]] == 0):
                del(sh[gems[lt]])
            lt += 1
            
    return answer
