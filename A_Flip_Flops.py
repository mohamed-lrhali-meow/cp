n = int(input())

for _ in range(n): 
    x , c , k = map(int,input().split())
    monsters = list(map(int,input()))
    for i in monsters : 
        if i > c : 
            print(c)
            continue 
        else : 
            for j in range(1,k) :
                if i + 1 <= c : 
                    i += 1 
                else : 
                    break 
            c += i
        print(c)