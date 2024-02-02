# format이 관건.
# N번째 소수점 자리까지 출력을 원하면 '{:.Nf}'.format(N)
# 앞 자리에 0을 추가하고 싶으면 '{:02d}'.format(N)
import sys

N, K = map(int, sys.stdin.readline().split())
scores = list(map(int, sys.stdin.readline().rstrip().split()))
intervals = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(K)]

for start, end in intervals:
    sliced_scores = scores[start-1: end]
    avg = sum(sliced_scores) / len(sliced_scores)
    converted_avg = '{:.2f}'.format(avg)
    print(converted_avg)
