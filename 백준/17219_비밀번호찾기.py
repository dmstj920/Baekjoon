import sys

n, m = map(int, input().split())
password = {}

for i in range(n):
    site, pw = sys.stdin.readline().split()
    password[site] = pw

for j in range(m):
    site = input()
    print(password[site])
