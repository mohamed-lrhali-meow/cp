n = int(input())
for i in range(n): 
    m = int(input())
    out = list(pow(x,2)for x in range(1,m+1))
    print(*out)