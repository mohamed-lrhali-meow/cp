import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t): 
    s = int(input().strip())
    print(s//10 + s%10)