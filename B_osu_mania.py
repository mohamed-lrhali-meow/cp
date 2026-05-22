import sys
input = sys.stdin.readline
output = sys.stdout.write

t = int(input())

for _ in range(t) : 
    x = int(input())
    a = []
    idx = []
    for i in range(x) : 
        a.append(input())
        idx.append(a[i].index("#") + 1)
    print(*idx[::-1])