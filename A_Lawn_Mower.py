x = int(input())

for _ in range(x): 
    n , w = map(int,input().split())
    removed = 0
    counter = 0
    print(n-(n//w))