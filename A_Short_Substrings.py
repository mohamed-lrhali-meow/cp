n = int(input())
for _ in range(n): 
    s = input()
    out = ''
    for i in range(len(s)-1):
        if s[i]!=s[i+1] : 
            out += s[i]
    print(out+)