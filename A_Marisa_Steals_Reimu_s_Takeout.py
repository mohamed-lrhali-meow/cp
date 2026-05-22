n = int(input())

for _ in range(n) : 
    x = int(input())
    w = list(map(int,input().split()))
    c = 0
    for i in range(len(w)) : 
        if w[i]%3 == 0 : 
            w.pop(w[i])
            c+=1
        else: 
            for j in range(i+1,x) : 
                if w[i] + w[j] % 3 == 0 : 
                    w.pop(w[i])
                    w.pop(w[j])
                    c+=1       
    print(c)