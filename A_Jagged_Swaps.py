n = int(input())

for _ in range(n) : 
    x = int(input())
    print("YES") if list(map(int,input().split()))[0] == 1 else print("NO")