n = int(input())
sum = 0
for i in range(1,n+1) : 
    sum += pow(-1,i) * i 

print(sum)