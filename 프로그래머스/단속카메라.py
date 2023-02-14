#강의 참고

def solution(routes):
    answer = 1
    routes.sort(key = lambda x:x[1])
    point = routes[0][1]
    
    for k in range(1, len(routes)):
        if point < routes[k][0]:
            point = routes[k][1]
            answer += 1
            
    return answer
