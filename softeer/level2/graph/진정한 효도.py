# 그래프 전치(transpose)와 단순 구현
# 그래프 전치(transpose) 시에 zip을 활용하는 것이 큰 도움이 된다.
# zip은 두 개 또는 그 이상의 iterable에서 각 요소를 뺴어와서 tuple들의 iterator로 변환해준다.
import sys

N = 3
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
answer = 2

ALL_DIFFERENT = 3
ALL_SAME = 1
ELEMENT_ONE = 1
ELEMENT_THREE = 3

def calculate_cost(ground):
    unique_n = len(set(ground))
    if unique_n == ALL_DIFFERENT:
        return 2
    elif unique_n == ALL_SAME:
        return 0
    elif ELEMENT_ONE in ground and ELEMENT_THREE in ground:
        return 2
    else:
        return 1

# Row
for row in graph:
    cost = calculate_cost(row)
    answer = min(answer, cost)

# Column
columns = [list(column) for column in zip(*graph)]
# columns = list(map(list, zip(*graph)))
for column in columns:
    cost = calculate_cost(column)
    answer = min(answer, cost)

print(answer)
