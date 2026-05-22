import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n , s , m = map(int,input().strip().split())
    tasks = []
    for i in range(n):
        l, r = map(int, input().split())
        tasks.append((l, r))
    tasks.sort()
    found  = False
    if tasks[0][0] - 0 >= s : 
        found = True
    for i in range(len(tasks) - 1):
        if tasks[i+1][0] - tasks[i][1] >= s:
            found = True
    if m - tasks[-1][1] >= s : 
        found = True
    if found : 
        print("YES")
    else : 
        print("NO")