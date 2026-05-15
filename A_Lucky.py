n = int(input())
for i in range(n): 
    s = input()
    if sum(map(int, s[:3])) == sum(map(int, s[3:])) : 
        print("YES")
    else : 
        print("NO")