K = int(input())

for i in range(K) : 
    n , m = map(int,input().split())
    points = 0
    positions = []
    for i in range(n) : 
        positions.append(list(map(int,input().split())))
    prev_t = 0
    prev_p = 0
    for t , p in positions : 
        dt = t - prev_t 
        dp = abs(p - prev_p) 
        if dt%2 == dp%2 : 
            points += dt 
        else : 
            points += dt -1
        prev_p = p 
        prev_t = t
    print(points + (m-prev_t))