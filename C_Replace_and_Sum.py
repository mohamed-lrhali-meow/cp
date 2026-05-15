import sys
input = sys.stdin.readline

x = int(input())
for _ in range(x):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a[n-1] = max(a[n-1], b[n-1])
    for i in range(n-2, -1, -1):
        a[i] = max(a[i], b[i], a[i+1])

    pre = [0]*(n+1)
    for i in range(n): 
        pre[i+1] = pre[i] + a[i] 
    
    out = []

    for i in range(q): 
        l , r = map(int,input().split())
        out.append(pre[r]-pre[l-1])
    print(*out)