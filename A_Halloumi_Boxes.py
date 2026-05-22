

x = int(input())

for _ in range(x): 
    n , k = map(int,input().split())
    nums = list(map(int,input().split()))
    if nums == sorted(nums) or k>=2 : 
        print("YES")
    else : 
        print("NO")