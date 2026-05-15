n = int(input())

for _ in range(n): 
    x = int(input())
    nums = list(map(int,input().split()))
    is_blocked = False
    for i in range(x) : 
        if sum(nums[:i]) == nums[i] : 
            nums[i] , nums[i-1]= nums[i-1] , nums[i]
            is_blocked = True
    if is_blocked : 
        print(*nums)
    else : 
        print(-1)