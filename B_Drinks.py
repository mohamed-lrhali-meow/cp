n = int(input())
pers = list(map(int,input().split()))
total = 0
for i in pers : 
    total += (1/n)*(i/100)

print(total*100)