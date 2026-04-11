n = int(input())
c = 0
i = 5
while n != 0 : 
    while n >= i : 
        n -= i 
        c +=1
    i -=1    

print(c)
    