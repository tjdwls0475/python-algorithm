# 시간 초과 유도 문제. for loop 내부에서 String Concatenation을 이용해서 정답을 구할 경우, 시간 초과(5초)가 발생한다.
# 그 이유는 String이 immutable한 특성을 지니고 있기 때문이다. 때문에 String을 덧붙일 때마다 새로운 String이 생성된다고 보면 된다.
# loop iteration 수가 500,000회이므로 String Concatenation은 적절치 않다.
# 반면에 List는 mutable한 특성을 지니고 있기 때문에, 아래와 같이 loop iteration 수가 많을 때 연산 시간을 획기적으로 줄일 수 있다.

import sys

N = int(sys.stdin.readline())
string_pairs = [sys.stdin.readline().rstrip().split() for _ in range(N)]
# answer = ""
answer = []

for S, T in string_pairs:
    for s_idx, s in enumerate(S):
        if s == 'X' or s == 'x':
            # answer += T[s_idx]
            answer.append(T[s_idx])
            break
answer = ''.join(answer)
print(answer.upper())

    
