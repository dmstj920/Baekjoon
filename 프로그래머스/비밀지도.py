def dtb(k, n):
    res = ""
    rem = ""
    while(k > 0) :
        if (int(k%2) == 1) :
            rem = "#" 
        else:
            rem = " "
        res = rem + res
        k = int(k/2)
    
    while(len(res) != n):
        res = " " + res
    
    return res


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(dtb(arr1[i] | arr2[i], n))

    return answer
