n = int(input())
for _ in range(n): 
    x = int(input())
    s = list(input())
    seen = set()
    b = 0
    for  i in s : 
        if i in seen : 
            b +=1 
        else : 
            b+=2 
            seen.add(i)
    print(b)