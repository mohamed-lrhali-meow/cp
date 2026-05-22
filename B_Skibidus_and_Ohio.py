n = int(input())
def adj(s):
    for i in range(len(s)-1): 
        if s[i] == s[i+1] : 
            return True
    return False
for _ in range(n) : 
    s  = input()
    l = len(s)
    u = set(s)
    idx = 0
    if not adj(s) : 
        print(l)
    else : 
        print(1)