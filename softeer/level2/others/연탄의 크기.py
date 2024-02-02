import sys

N = int(sys.stdin.readline())
radiuses = list(map(int, sys.stdin.readline().split()))

M = max(radiuses)
answer = 0

for r in range(2, M+1):
    check_list = list(map(lambda x: x % r, radiuses))
    if check_list.count(0) > answer:
        answer = check_list.count(0)
        
print(answer)
