import sys

# Define Variables
answer = 0

# Taking Inputs
back_weight, n = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# Sort by its price
table.sort(key=lambda x: x[1], reverse=True)

# Calculate by using Greedy algorithm
for m, p in table:
    if back_weight <= m:
        answer += back_weight * p
        break
    else:
        answer += m * p
        back_weight -= m

print(answer)
