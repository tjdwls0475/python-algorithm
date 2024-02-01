import sys

m, n, k = map(int, sys.stdin.readline().split())
secret_n = list(map(int, sys.stdin.readline().split()))
user_input = list(map(int, sys.stdin.readline().split()))

if m > n:
    print("normal")
else:
    is_secret = False
    for i in range(n-m+1):
        # Compare sublists
        if user_input[i:i+m] == secret_n:
            print("secret")
            is_secret = True
            break
    if not is_secret:
        print("normal")
