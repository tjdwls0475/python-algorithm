import sys

n = int(sys.stdin.readline())
cases = [sys.stdin.readline().split() for _ in range(n)]

digit_dict = {
'1': [0,0,0,0,1,1,0],
'2': [1,0,1,1,0,1,1],
'3': [1,0,0,1,1,1,1],
'4': [0,1,0,0,1,1,1],
'5': [1,1,0,1,1,0,1],
'6': [1,1,1,1,1,0,1],
'7': [1,1,0,0,1,1,0],
'8': [1,1,1,1,1,1,1],
'9': [1,1,0,1,1,1,1],
'0': [1,1,1,1,1,1,0],
'-': [0,0,0,0,0,0,0]
}

def subtraction(o, p):
    sum = 0
    for q, r in zip(digit_dict[o], digit_dict[p]):
        sum += abs(q-r)
    return sum

for i, j in cases:
    if len(i) == len(j):
        sum = 0
        for k, l in zip(i, j):
            sum += subtraction(k, l)
        print(sum)
    elif len(i) > len(j):
        sum = 0
        for k in range(1, min(len(i), len(j))+1):
            sum += subtraction(i[-k], j[-k])
        for l in range(len(i)-len(j)):
            sum += subtraction(i[l], '-')
        print(sum)
    else:
        sum = 0
        for k in range(1, min(len(i), len(j))+1):
            sum += subtraction(i[-k], j[-k])
        for l in range(len(j)-len(i)):
            sum += subtraction(j[l], '-')
        print(sum)
