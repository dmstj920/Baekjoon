def solution(s):
    str = list(map(int, s.split()))
    str.sort()
    
    answer = "{} {}".format(str[0], str[-1])
    return answer
