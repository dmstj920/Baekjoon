from collections import defaultdict

n = int(input())

log = defaultdict(list)
for i in range(n):
    name, company = input().split()
    log[name].append(company)

answer = sorted(log.keys(), reverse=True)
for answer_ in answer:
    print(answer_)

