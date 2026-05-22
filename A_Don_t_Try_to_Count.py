import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n , m = map(int,input().strip().split())
    p = input().strip()
    s = input().strip()
    c =0 
    while not(s in p):
        if len(p) >= m + n:
            print(-1)
            break
        p += p
        c += 1
    else:
        print(c)