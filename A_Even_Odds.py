k , n = map(int,input().split())
new = []
for i in range(k//2): 
    new.append(2*i +1)
for i in range(k//2) :
    new.append(2*i)
print(new[n-1])