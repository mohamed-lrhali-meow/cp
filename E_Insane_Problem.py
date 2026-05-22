import math

t = int(input())

for _ in range(t) : 
    k , l1 , r1 , l2 , r2 = map(int,input().split())
    ans = 0
    m = 1
    for n in range(31) : 
        lo = max(l1, math.ceil(l2 / m))
        hi = min(r1, math.floor(r2 / m))
        if lo <= hi : 
            ans += hi - lo +1  
        m *= k 
        
    print(ans)
            