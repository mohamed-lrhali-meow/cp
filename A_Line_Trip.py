k = int(input())

for _ in range(k) : 
    n , x = map(int,input().split())
    fuel = [0] + list(map(int,input().split()))
    m = 0 
    for i in range(n): 
        m = max(m,fuel[i+1]-fuel[i])

    m = max(m,(x-fuel[-1])*2)
    print(m)