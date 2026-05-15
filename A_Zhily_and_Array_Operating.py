n = int(input())

for _ in range(n): 
    x = int(input())
    nums = list(map(int,input().split()))
    c = 0
    nums = nums[::-1]
    for i in range(1,x): 
        if nums[i-1] > 0 : 
            nums[i] += nums[i-1]
    for i in nums : 
        if i > 0 : 
            c +=1 
    print(c)