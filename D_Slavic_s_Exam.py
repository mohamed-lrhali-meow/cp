import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = list(input().strip())
    t = list(input().strip())
    idx_s = 0
    idx_t = 0
    while idx_s <= len(s)-1 and idx_t <= len(t)-1 : 
        if s[idx_s] == t[idx_t] : 
            idx_s +=1 
            idx_t +=1 
        elif s[idx_s] == '?' : 
            s[idx_s] = t[idx_t]
            idx_s +=1 
            idx_t +=1
        else : 
            idx_s +=1 
    for i in range(len(s)) : 
        if s[i] == '?' : 
            s[i] = 'a'
    if  idx_t == len(t) : 
        print("YES")
        print(''.join(s))
    else : 
        print("NO")