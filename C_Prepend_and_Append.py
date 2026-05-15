n = int(input())

for _ in range(n): 
    x = int(input())
    s = input()
    out = len(s)
    for i in range(len(s)//2) : 
        if s[i] != s[-i-1] : 
            out -= 2
        else : 
            break
    print(out)