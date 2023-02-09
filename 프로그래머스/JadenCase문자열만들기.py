def solution(s):
    s = s.lower()
    answer = ''
    flag = 0

    for i in range(len(s)):
        if s[i] == " ":
            flag = 1
            answer += s[i]
            
        elif flag == 1 or i == 0:
            t = s[i].upper()
            flag = 0
            answer += t
        
        else:
            answer += s[i]
    
    return answer
