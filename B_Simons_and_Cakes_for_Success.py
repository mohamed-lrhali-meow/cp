x = int(input())

for _ in range(x):
    n = int(input())
    k = 1
    for i in range(2,1000000) : 
        if (i^n)%n == 0 : 
            k = i
            break 
    print(k)