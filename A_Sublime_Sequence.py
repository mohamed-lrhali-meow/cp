n = int(input())

for _ in range(n): 
    x , k = map(int,input().split())
    if k%2 == 0 : 
        print(0)
    else : 
        print(x)