n = int(input())
for _ in range(n): 
    x = int(input())
    nums = list(map(int,input().split()))
    nums_unique = set(nums)
    if len(nums_unique) >2 : 
        print("No")
    else : 
        nums.sort()
        if abs(nums.count(nums[0])-nums.count(nums[-1])) <=1 :
            print("Yes")
        else : 
            print("No")