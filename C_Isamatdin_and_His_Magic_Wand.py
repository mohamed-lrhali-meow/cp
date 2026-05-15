n = int(input())
for _ in range(n): 
    x= int(input())
    nums = list(map(int,input().split()))
    for i in range(x-1) : 
        for j in range(i,x) :
            if nums[i]%2 != nums[j]%2 and (nums[j]<nums[i]): 
                temp = nums[j]
                nums[j] = nums[i] 
                nums[i] = temp
    print(" ".join(map(str,nums)))