x = int(input())
def is_sorted(nums): 
    for i in range(len(nums)-1): 
        if nums[i]>nums[i+1] : 
            return False 
    return True
for _ in range(x) : 
    n , m = map(int,input().split())
    nums = list(map(int,input().split()))
    b = int(input())

    nums[0] = min(nums[0], b - nums[0])
    for i in range(1,n) : 
        if nums[i] >= nums[i-1] : 
            if (b - nums[i]) >= nums[i-1] : 
                nums[i] = min(nums[i],b - nums[i])
        elif (b - nums[i]) >= nums[i-1] : 
            nums[i] = (b - nums[i])
        else : 
            print("NO")
            break
    if (is_sorted(nums)) : 
        print("YES")
    