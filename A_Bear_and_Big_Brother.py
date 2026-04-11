nums = list(map(int,input().split()))
c = 0

while nums[0] <= nums[1]: 
    nums[0] *= 3
    nums[1] *= 2 
    c +=1 

print(c)