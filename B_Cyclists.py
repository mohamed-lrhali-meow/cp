x = int(input())

for _ in range(x): 
    n , k , p , m = map(int,input().split())
    nums = list(map(int,input().split()))
    wincon = nums[p-1] 
    c = 0
    out = False
    while m >0 and (not out) :
        found = False
        for i in range(k): 
            if nums[i] == wincon : 
                if i > m :
                    out = True
                else  :    
                    m -= i 
                    c += 1
                found = True
        if not found : 
            m -= nums[0]
            temp = nums[0]
            nums.pop(0)
            nums.append(temp)
            
    print(c)