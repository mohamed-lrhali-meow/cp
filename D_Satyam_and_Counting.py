import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    xs = {}
    for i in range(n):
        x, y = map(int, input().split())
        xs[x] = xs.get(x, 0) + 1
    
    pairs = sum(1 for v in xs.values() if v == 2)
    print(pairs * (n - 2))