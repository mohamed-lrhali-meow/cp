n = int(input())
for _ in range(n): 
    x = int(input())
    nums = list(map(int,input().split()))
    p = 0
    o = 0
    for  i in range(x)  : 
        if nums[i] %2 == 0 : 
            p += 1
        else : 
            o += 1
    if o %2 == 0 : 
        print("YES")
    else : 
        print("NO")
