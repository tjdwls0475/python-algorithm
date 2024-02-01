import sys

# 시간초과 주의. 거듭제곱 연산자 ** 사용시 시간초과
k, p, n = map(int, sys.stdin.readline().split())
answer = k

for i in range(n):
    answer *= p
    answer %= 1000000007

print(answer)
