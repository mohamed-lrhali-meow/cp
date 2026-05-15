n = int(input())
for _ in range(n): 
    x = int(input())
    nums = list(map(int,input().split()))
    if x  == 1 : 
        print(1)
    else : 
        for  i in range(x): 
            print(2 , end=' ')
        print("\n")
        
