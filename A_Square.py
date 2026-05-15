n = int(input())
for _ in range(n): 
    s = list(input().split())
    if s.count(s[0]) == 4 : 
        print("YES")
    else : 
        print("NO")