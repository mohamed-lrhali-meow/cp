n = int(input())

for _ in range(n) : 
    name = list(input().split())
    out = ''
    for i in range(len(name)) : 
        out += name[i][0]
    print(out)