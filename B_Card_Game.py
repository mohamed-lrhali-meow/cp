import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a1,a2,b1,b2 = map(int,input().strip().split())
    c = 0
    rounds = [
        (a1,b1,a2,b2),
        (a1,b2,a2,b1),
        (a2, b1, a1, b2),
        (a2, b2, a1, b1) ]
    for t1,t2,t3,t4 in rounds : 
        r1 = 1 if (t1>t2) else (-1 if t1 < t2 else 0)
        r2 = 1 if (t3>t4) else (-1 if (t3 < t4) else 0)
        if (r1 + r2) > 0 : 
            c +=1

    print(c)