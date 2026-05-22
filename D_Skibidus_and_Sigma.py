x = int(input())

for _ in range(x) : 
    n , m = map(int,input().split())
    nums = []
    arrays = []
    s = 0
    for i in range(n) : 
        arrays.append(list(map(int,input().split())))
    arrays.sort(key=sum, reverse=True) 
    for array in arrays : 
        nums += array 
    for i in range(len(nums)) : 
        s += nums[i] * (len(nums)-i)
    print(s)