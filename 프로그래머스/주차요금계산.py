import math

#강의 참조
def calculate(time):
    hour, minute = time.split(":")
    total = int(hour) * 60 + int(minute)
    
    return total
    
    
def solution(fees, records):
    inTime = [0]*10000
    isIn = [0]*10000
    sumT = [0]*10000
    
    cars = []
    for i in records:
        a, b, c = i.split()
        b = int(b)
        cars.append(b)            
            
        if c == "IN":
            inTime[b] = calculate(a)
            isIn[b] = 1
        else:
            sumT[b] += calculate(a) - inTime[b]
            isIn[b] = 0
            
    
    cars = sorted(set(cars))
    answer = []
    for j in cars:
        if isIn[j] == 1:
            sumT[j] += calculate("23:59") - inTime[j]
        
        fee = fees[1]+ max(math.ceil((sumT[j]-fees[0])/fees[2]),0) * fees[3]
        answer.append(fee) 
    
    return answer

#내 코드
"""def calculate(hour1, minute1, hour2, minute2):
    hour1, minute1, hour2, minute2 = int(hour1), int(minute1), int(hour2), int(minute2)
    minute = minute2 - minute1
    hour = hour2 - hour1
    if minute < 0:
        minute += 60
        hour -= 1
    
    total = hour * 60 + minute
    
    return total


def solution(fees, records):
    test = [0]*10000
    cars = []
    total = 0
    for i in records:
        time, car, inform = i.split()
        cars.append(int(car))
        if test[int(car)] != 0:
            if test[int(car)][2] == "IN":
                inTime = test[int(car)][0]
                outTime = time
                hour1, minute1 = inTime.split(":")
                hour2, minute2 = outTime.split(":")
                test[int(car)][1] += calculate(hour1, minute1, hour2, minute2)
                test[int(car)][2] = inform
                
            else:
                test[int(car)][0] = time
                test[int(car)][2] = inform                        

        else:
            test[int(car)] = [time, total, inform]
        
    answer = []
    cars = sorted(set(cars))
    for j in cars:
        carTotal = test[j][1]
        carInform = test[j][2]
        carTime = test[j][0]
        money = 0
        
        if carInform == "IN":
            hour1, minute1 = carTime.split(":")
            carTotal += calculate(hour1, minute1, "23", "59")
            
        if carTotal <= fees[0]:
            money = fees[1]
        else:
            money += fees[1]
            money += math.ceil((carTotal - fees[0]) / fees[2]) * fees[3]

        answer.append(money)
            
        
    return answer
    """
