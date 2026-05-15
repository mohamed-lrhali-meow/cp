    # lawnmower switchs when the number of dandelions is odd 
    # we want to cut the max num of dandelions 
    # we can go to the biggest off num to turn the lawnmower then go over all even nums 
    # then if its on go to the biggest odd num else go the smallest odd num 

n = int(input())
for _ in range(n):
    x = int(input())
    fields = list(map(int, input().split()))
    odd = sorted([k for k in fields if k % 2 == 1], reverse=True)
    even = [k for k in fields if k % 2 == 0]
    
    
    if odd : 
        print(sum(even)+sum(odd[::2]))
    else : 
        print(0)