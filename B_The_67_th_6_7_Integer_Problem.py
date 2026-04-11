n = int(input())
for i in range(n): 
    nums = list(map(int,input().split()))
    nums.sort()
    nums[:6] = [-x for x in nums[:6]]
    print(sum(nums))