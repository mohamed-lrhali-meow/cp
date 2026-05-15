# i have an array a , and a sub-araay of a bitween index l,r -> a[l,r]
# i have k multisets 
# if ai is in the subarray i put it in the multiset number 1 else i put it where ever i want 
# i want to find a subarray such that all multisets have the same elements 

x = int(input())

for _ in range(x) : 
    n , k = map(int,input().split())
    nums = list((input().split()))
    count = {}
    for i in range(n) : 
        count[nums[i]] += 1 