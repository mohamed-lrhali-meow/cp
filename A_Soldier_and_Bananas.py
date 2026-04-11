k,n,w = map(int, input().split())

c = 1
while c <= w : 
    n -= c * k 
    c +=1
print(-n if n<0 else 0)