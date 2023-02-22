def solution(s):
    pCount = 0
    yCount = 0
    answer = True
    
    s = s.lower()
    
    for i in range(len(s)):
        if s[i] == "p":
            pCount += 1
        
        elif s[i] == "y":
            yCount += 1
            
    if pCount != yCount:
        answer = False

    return answer
