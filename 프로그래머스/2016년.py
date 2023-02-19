def solution(a, b):
    answer = ''
    mlist = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    cnt = 0
    
    for i in range(a-1):
        cnt += mlist[i]
    cnt += b
    cnt %= 7
    
    answer = day[cnt-1]
    
    return answer
