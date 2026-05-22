n = int(input())

for _ in range(n) : 
    m,a,b,c = map(int,input().split())
    monkey = 0
    row1 = min(a,m) 
    row2 = min(b,m)
    leftover = max(0,m-a) + max(0,m-b)
    monkey = row1 + row2 + min(c,leftover)
    print(monkey)