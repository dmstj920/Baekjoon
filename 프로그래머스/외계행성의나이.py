def solution(age):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    answer = ''
    
    for i in str(age):
        answer += alphabet[int(i)]
        
    return answer
