x = int(input())

for _ in range(x) : 
    n , m , l , r = map(int,input().split())
    d = n-m
    
    remove_right  = min(d,r )
    remove_left = d - remove_right

    print(l + remove_left , r - remove_right)