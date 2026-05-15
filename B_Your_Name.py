from collections import Counter
n = int(input())

for _ in range(n): 
    x = int(input())
    names  = list(input().split())
    c1 = Counter(names[0])
    c2 = Counter(names[1])
    if c1 == c2 : 
        print("YES")
    else : 
        print('NO')