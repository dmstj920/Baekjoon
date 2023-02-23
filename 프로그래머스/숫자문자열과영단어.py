def solution(s):
    word = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5,
            "six":6, "seven":7, "eight":8, "nine":9}
    
    key = ""
    answer = ""
    for i in range(len(s)):
        if ord(s[i]) >= 48 and ord(s[i]) <= 57:
            answer += s[i]
        else:
            key += s[i]
        
        value = word.get(key)
        if value != None:
            answer += str(value)
            key = ""
            
    return int(answer)
  
  #문자열 => 아스키: ord()
  #딕셔너리에서 key값으로 value 가져오기: get()
