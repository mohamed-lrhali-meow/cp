x = int(input())
def is_sorted(nums): 
    for i in range(len(nums)-1): 
        if nums[i]>nums[i+1] : 
            return False 
    return True

def binary_search(b,target): 
    l = 0
    r = len(b)-1
    result = -1
    while l<=r : 
        mid = (l+r)//2
        if b[mid] >= target : 
            result = mid
            r = mid -1
        else : 
            l = mid +1 
    return result 

for _ in range(x) : 
    n , m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    b.sort()
    option1 = a[0]
    option2 = b[0] - a[0]  
    a[0] = min(option1, option2)
    for i in range(1,n): 
        option1 = a[i]
        target = a[i-1] + a[i]
        idx = binary_search(b,target)
        if idx != -1 : 
            option2 = b[idx] - a[i]
        else : 
            option2 = None
        
        if option1 >= a[i-1] : 
            if option2 is not None and option2 >= a[i-1]: 
                a[i] = min(option1,option2)
            else : 
                a[i] = option1
        elif option2 is not None and option2 >= a[i-1]: 
            a[i] = option2
        else : 
            print("NO")
            break
    if is_sorted(a) : 
        print("YES")
        
    