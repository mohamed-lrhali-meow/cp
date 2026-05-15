n = int(input())

for _ in range(n): 
    x = int(input())
    nums = list(input().split())
    c = nums.count('2')
    counter = 0
    if c %2 == 1 : 
        print(-1)
    elif c == 0 : 
        print(1)
    else: 
        for idx in range(len(nums)) : 
            if nums[idx] == '2' : 
                counter += 1 
            if counter == (c//2): 
                print(idx + 1)
                break